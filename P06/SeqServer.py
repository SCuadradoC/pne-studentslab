import http.server
import socket
import socketserver
from Seq1 import *
import os
#from config import *
import termcolor

# Define the Server's port
IP = "127.0.0.1" #socket.gethostbyname(socket.gethostname())
PORT = 8080
PATH = "./P06/html"
GENE_DIR = "./sequences/"
LNK = f"http://{IP}:{PORT}"

seqs = ["ATCGTACAGTCTGACTAGTCGGGGGTG",
        "TAGCGGGTCATGGGATCATATCGATGCTGCATTATT",
        "GCGAGCGATAGCAGTCTAGCTACGTA",
        "AGCGCGCGCCGTACGTGTCGTGCTATCGATCGTACGTCGATCGCGTAGTC",
        "TCTCGTAGCGAGAGCTAGCTAGTCCTTAGCTAGCGTGAGC"]

gene_files = os.listdir(GENE_DIR) #check after changing seq module
genes = {}
for e in gene_files:
    genes.update({e.split(".")[0] : GENE_DIR + e}) #this takes only the name of the gene from the list of gene files, and the directory where that file is
#print(genes)

class TestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)
        
        try:
            if self.path in ["/","/index.html"]:
                page = open(PATH + "/index.html")
                contents = page.read()
                page.close()
                
                contents = contents.replace("[[lnk]]", LNK)
                options = ""
                for e in range(0,len(seqs)):
                    options += f'<option value="{e}">{e}</option> '
                contents = contents.replace("[[options]]",options)

                style = "text/html"
            elif self.path == "/logo.png":
                page = open(PATH + "favicon.ico", "rb")
                contents = page.read()
                style = "image/png"

            elif "/echo" in self.path:
                print(self.path)
                if "get_sequence" in self.path:
                    sequence_num = int(self.path.split("=")[1])
                    contents = f"""<p>Sequence requested:</p> <p>{seqs[sequence_num]}</p> <a href="{LNK}">Main page</a>"""
                    style = "text/html"
            else:
                page = open(PATH + self.path + ".html")
                contents = page.read()
                page.close()
                contents = contents.replace("[[lnk]]", LNK)
                style = "text/html"
            response_code = 200
        except FileNotFoundError:
            page = open(PATH + "/error.html")
            contents = page.read()
            page.close()
            style = "text/html"
            response_code = 404
        
        
        self.send_response(response_code)
        
        termcolor.cprint(self.requestline, 'green')
        #print(contents)
        
        self.send_header('Content-Type', style)
        
        if style == "text/html":
            # Define the content-type header:
            self.send_header('Content-Length', len(contents.encode()))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(contents.encode())
        elif style == "image/png":
            self.end_headers()
            self.wfile.write(contents)
            
            

        return

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    print("Serving at PORT", PORT) # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()





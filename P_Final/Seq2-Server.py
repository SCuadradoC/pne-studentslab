import http.server
#import socket
import socketserver
from Seq1 import *
import os
#from config import *
import termcolor
from html_helper import *



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
                options = ""
                for e in range(0,len(seqs)):
                    options += f'<option value="{e}">{e}</option> '
                contents = contents.replace("[[options_seq]]",options)
                options = ""
                for e in genes:
                    options += f'<option value="{e}">{e}</option> '
                contents = contents.replace("[[options_gene]]",options)

                style = "text/html"
#            elif self.path == "/favicon.ico":
#                page = open(PATH + "/logo.png", "rb")
#                contents = page.read()
#                style = "image/png"

            elif "/echo" in self.path:
                print(self.path)
                if "get_sequence" in self.path:
                    req_val = int(self.path.split("=")[1])
                    file = open(PATH + "/get.html")
                    page_raw = file.read()
                    file.close()
                    contents = insert_content(page_raw,["n","seq_cont"],[str(req_val),seqs[req_val]])
                    style = "text/html"
                elif "get_gene" in self.path:
                    req_val = self.path.split("=")[1]
                    file = open(genes[req_val])
                    gene_raw = file.read().split("\n")
                    file.close()
                    file = open(PATH + "/gene.html")
                    page_raw = file.read()
                    file.close()
                    gene_proc = ""
                    for e in gene_raw:
                        gene_proc += f"{e}<br> "
                    contents = insert_content(page_raw,["gene_name","gene_cont"],[req_val,gene_proc])
                    file.close()
                    style = "text/html"
            elif "operation" in self.path:
                req_val = self.path.split("?")[1].split("&")
                seq_in = Seq(req_val[0].split("=")[1],False)
                operation = req_val[1].split("=")[1]

                if operation == "Info":
                    bases = seq_in.count()
                    l = len(seq_in)
                    if l != 0:
                        result = f"""<p>Total length: {l}</p>
<p>A: {bases["A"]} ({bases["A"] / l * 100}%)</p>
<p>C: {bases["C"]} ({bases["C"] / l * 100}%)</p>
<p>T: {bases["T"]} ({bases["T"] / l * 100}%)</p>
<p>G: {bases["G"]} ({bases["G"] / l * 100}%)</p>"""
                    else:
                        seq_in = req_val[0].split("=")[1]
                        result = "Erroneous sequence"
                    
                elif operation == "Complement":
                    result = str(seq_in.complement())
                elif operation == "Reverse":
                    result = str(seq_in.reverse())
                file = open(PATH + "/operation.html")
                page_raw = file.read()
                file.close()
                
                contents = insert_content(page_raw,["seq_in","operation","result"],[str(seq_in),operation,result])
                style = "text/html"
            else:
                page = open(PATH + self.path + ".html")
                contents = page.read()
                page.close()
                
                style = "text/html"
            response_code = 200
        except FileNotFoundError:
            page = open(PATH + "/error.html")
            contents = page.read()
            page.close()
            style = "text/html"
            response_code = 404
        
        contents = contents.replace("[[lnk]]", LNK)
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





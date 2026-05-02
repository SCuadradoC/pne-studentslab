import http.server
import http.client
import json
#import socket
import socketserver
import os
#from config import *
import termcolor

# my custom libraries:
from Seq1 import *
from html_helper import *
import per_page_code as ppc



# Define the code parameters
IP = "127.0.0.1" #socket.gethostbyname(socket.gethostname())
PORT = 8080
PATH = "./P_Final/html"
GENE_DIR = "./sequences/"
LNK = f"http://{IP}:{PORT}"
SERVER = "rest.ensembl.org"
PAGES = ["/listSpecies","/karyotype","/chromosomeLength"]

conn = http.client.HTTPConnection(SERVER)

class TestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)
        dir_path, params = parse_req(self.path)
        try:
            if dir_path == "/" or dir_path == "/index.html":
                contents = load_txt(PATH + "/index.html")
                style = "text/html"
#            elif dir_path == "/favicon.ico":
#                page = open(PATH + "/logo.png", "rb")
#                contents = page.read()
#                style = "image/png"
            elif dir_path == PAGES[0]:
                contents = ppc.listSpecies(params)
                style = "text/html"
            elif dir_path == PAGES[1]:
                contents = ppc.karyotype(params)
                style = "text/html"
                
            #style = "text/html"
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





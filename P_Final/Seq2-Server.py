import http.server
import http.client
import json
#import socket
import socketserver
from Seq1 import *
import os
#from config import *
import termcolor
from html_helper import *
import per_page_code as ppc



# Define the code parameters
IP = "127.0.0.1" #socket.gethostbyname(socket.gethostname())
PORT = 8080
PATH = "./P_Final/html"
GENE_DIR = "./sequences/"
LNK = f"http://{IP}:{PORT}"
SERVER = "http://rest.ensembl.org"

conn = http.client.HTTPConnection(SERVER)

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
                style = "text/html"
#            elif self.path == "/favicon.ico":
#                page = open(PATH + "/logo.png", "rb")
#                contents = page.read()
#                style = "image/png"

            else:# "/echo" in self.path
                print(self.path)
                endpoint, params = parse_req(self.path)
                pos_endpoints = ["/listSpecies","/karyotype","/chromosomeLength"]
                if endpoint == pos_endpoints[0]:
                    ppc.listSpecies(params)
            
            page = open(PATH + self.path + ".html")
            contents = page.read()
            page.close()
                
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





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
import per_page_class as ppc



# Define the code parameters
IP = "127.0.0.1" #socket.gethostbyname(socket.gethostname())
PORT = 8080
PATH = "./P_Final/html"
GENE_DIR = "./sequences/"
LNK = f"http://{IP}:{PORT}"
SERVER = "rest.ensembl.org"
PAGES = ["/listSpecies","/karyotype","/chromosomeLength", "/geneLookup", "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]



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
                response_code = 200
            else:
                if dir_path == PAGES[0]:
                    req = ppc.listSpecies(params,PATH)
                elif dir_path == PAGES[1]:
                    req = ppc.karyotype(params,PATH)
                elif dir_path == PAGES[2]:
                    req = ppc.chromosomeLenght(params,PATH)
                elif dir_path == PAGES[3]:
                    req = ppc.geneLookup(params,PATH)
                elif dir_path == PAGES[4]:
                    req = ppc.geneSeq(params,PATH)
                elif dir_path == PAGES[5]:
                    req = ppc.geneInfo(params,PATH)
                elif dir_path == PAGES[6]:
                    req = ppc.geneCalc(params,PATH)
                elif dir_path == PAGES[7]:
                    req = ppc.geneList(params,PATH)
                else:
                    req = ppc.error(PATH)
                
                try:
                    if params["json"] == "1":
                        contents, style  = req.json()
                    else:
                        contents, style  = req.html()
                except KeyError:
                    contents, style  = req.html()
                response_code = req.response_code()

        except FileNotFoundError:
            page = open(PATH + "/error.html")
            contents = page.read()
            page.close()
            style = "text/html"
            response_code = 404
        
        contents = contents.replace("[[lnk]]", LNK)

        self.send_response(response_code)
        self.send_header('Content-Type', style)

        #termcolor.cprint(self.requestline, 'green')
        print(contents)
        if style == "text/html":
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()

            # Send the response message
            self.wfile.write(contents.encode())

        elif style == "application/json":
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()

            # Send the response message
            self.wfile.write(str.encode(contents))

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





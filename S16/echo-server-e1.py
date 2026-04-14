import http.server
import socket
import socketserver
import termcolor
from pathlib import Path

from urllib.parse import parse_qs, urlparse
import jinja2 as j

def read_html_file(filename):
    contents = Path(PATH + "html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


# Define the Server's port
IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
PATH = "./S16/html/"

class TestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)
        
        try:
            if self.path == "/":
                page = open(PATH + "form-e1.html")
                contents = page.read()
                page.close()
                style = "text/html"
                icon = "quest.png"
            elif "/echo" in self.path:
                #page = open(PATH + "echo-server-e1.html")
                #contents = page.read()
                #page.close()
                url_path = urlparse(PATH + "echo-server-e1.html")
                path = url_path.path # we get it from here
                arguments = parse_qs(url_path.query)
                text = arguments
                print(text)
                contents = read_html_file(PATH + "echo-server-e1.html").render(context={"todisplay": text}) # provide a dictionary to build the form
                style = "text/html"
                icon = "res.png"
            elif self.path == "logo.png":
                page = open(PATH + icon, "rb")
                contents = page.read()
                style = "image/png"
            else:
                page = open(PATH + self.path)
                contents = page.read()
                page.close()
                style = "text/html"
            response_code = 200
        except FileNotFoundError:
            page = open(PATH + "error.html")
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
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT) # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()


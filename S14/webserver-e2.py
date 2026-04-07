import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080
PATH = "./S14/pages/"

class TestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)
        
        if self.path in["/","/index.html"]:
            self.send_response(200)
            page = open(PATH + "index.html")
            contents = page.read()
            page.close()
            style = "text/html"
        elif self.path == "/favicon.ico":
            self.send_response(200)
            page = open(PATH + "logo.png")
            contents = page.read()
            page.close()
            style = "image/png"
        else:
            self.send_response(200)
            page = open(PATH + "error.html")
            contents = page.read()
            page.close()
            style = "text/html"

        termcolor.cprint(self.requestline, 'green')

        # Define the content-type header:
        self.send_header('Content-Type', style)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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


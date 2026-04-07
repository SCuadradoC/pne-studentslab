import http.server
import socketserver

# Define the Server's port
PORT = 8080

class TestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)

        termcolor.cprint(self.requestline, 'green')

        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        contents = "I am the happy server! :-)"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
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


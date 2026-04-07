import http.server
import socketserver as ss

PORT = 8080


ss.TCPServer.allow_reuse_address = True
Handler = http.server.SimpleHTTPRequestHandler

with ss.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()

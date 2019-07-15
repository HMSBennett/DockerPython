import http.server
import socketserver

PORT = 9000
Handler = http.server.SimpleHTTPRequestHandler
https = socketserver.TCPServer(("", PORT), Handler)
print("serving at port: ", PORT)
https.serve_forever()

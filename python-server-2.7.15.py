import SimpleHTTPServer
import SockerServer

PORT = 9000
Handler = SimpleGTTPServer.SimpleHTTPRequestHandler
httpd = SockerServer.TCPServer(("", PORT), Handler)
https.serve_forever()

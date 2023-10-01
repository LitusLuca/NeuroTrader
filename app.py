'''from http.server import HTTPServer, BaseHTTPRequestHandler,SimpleHTTPRequestHandler
import argparse

#class SimpleServer(SimpleHTTPRequestHandler):
#    def _set_header(self):
#        self.send_response(200)
#        self.send_header("Content-type", "text/html")
#        self.end_headers()
#        
#    def _html(self, title, msg):
#        content = f"""
#        <html>
#        <head><title>{title}</title></head>
#        <body><h3>{msg}</h3></body>
#        </html>
#        """
#        return content.encode("utf8")
#
#    def do_GET(self):
#        if self.path == "/":
#            self._set_header()
#            print(self.path)
#            self.wfile.write(self._html("Hello World!", "Hi!"))
#        else:
#            self.path = "/public"+self.path
#            return SimpleHTTPRequestHandler.do_GET(self)
#
#
#    def do_HEAD(self):
#        self._set_header()
#
#def run(serverHandler=SimpleServer, addr="localhost",port=8080):
#    server_address = (addr, port)
#    webServer = HTTPServer(server_address, serverHandler)
#    print("Starting http server on {addr}:{port}")
#    try:
#        webServer.serve_forever()
#    except KeyboardInterrupt:
#        pass
#
#if __name__ == "__main__":
#    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
#    parser.add_argument(
#        "-p",
#        "--port",
#        type=int,
#        default=8080,
#        help="Specify the port on which the server listens",
#    )
#    args = parser.parse_args()
#    run(port=args.port)
'''


from flask import Flask, render_template

from api import bp as api

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

app.register_blueprint(api)
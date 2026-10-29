from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

PORT = int(os.environ.get('PORT', '3000'))

class SiteHandler(SimpleHTTPRequestHandler):
    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({'.js': 'application/javascript', '.css': 'text/css'})

    def log_message(self, fmt, *args):
        print(fmt % args)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = ThreadingHTTPServer(('0.0.0.0', PORT), SiteHandler)
    print(f'WGM Collective site listening on 0.0.0.0:{PORT}', flush=True)
    server.serve_forever()

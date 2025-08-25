from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        
        # Set headers
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        
        # JSON message
        message = {"message": "Welcome in JSON"}
        response = json.dumps(message).encode("utf-8")

        # Send response
        self.wfile.write(response)

    def log_message(self, format, *args):
        # Override to disable console logging (optional)
        return

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), SimpleHandler)
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
        server.server_close()


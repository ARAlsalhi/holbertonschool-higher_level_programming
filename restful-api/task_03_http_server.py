#!/usr/bin/python3
"""A simple API using Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests for the simple API."""

    def send_text_response(self, status_code, message):
        """Send a plain-text HTTP response."""
        response = message.encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def send_json_response(self, status_code, data):
        """Send a JSON HTTP response."""
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self.send_text_response(
                200,
                "Hello, this is a simple API!"
            )

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_json_response(200, data)

        elif self.path == "/status":
            self.send_text_response(200, "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_json_response(200, info)

        else:
            self.send_text_response(404, "Endpoint not found")


def run_server():
    """Start the HTTP server on port 8000."""
    server_address = ("", 8000)
    http_server = HTTPServer(server_address, SimpleAPIHandler)

    print("Server running on http://localhost:8000")

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        http_server.server_close()


if __name__ == "__main__":
    run_server()

import http.server
import socketserver
import uuid
import logging
from pystyle import Colors, Colorate

logging.basicConfig(filename='ip_logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

PORT = 8080


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/log/'):
            unique_id = self.path.split('/')[-1]
            ip_address = self.client_address[0]
            logging.info(f'Unique ID: {unique_id} - IP Address: {ip_address}')
            response = f"Your IP address ({ip_address}) has been logged with ID: {unique_id}"
        else:
            response = "Welcome! Go to /log/<unique_id> to log your IP address."

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))


def generate_unique_link():
    unique_id = str(uuid.uuid4())
    link = f"http://localhost:{PORT}/log/{unique_id}"
    print(Colorate.Horizontal(Colors.red_to_yellow, f"Generated link: {link}"))
    return link


def run_server():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Starting the IP Logger Server..."))
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Serving on port {PORT}"))
        httpd.serve_forever()

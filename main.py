from http.server import BaseHTTPRequestHandler, HTTPServer

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return 'Error: Division by zero'
        return a / b

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        calculator = Calculator()
        self.wfile.write(b'<html><body><h1>Calculator Webpage</h1>')
        self.wfile.write(b'<form action="/calculate" method="post">')
        self.wfile.write(b'<input type="number" name="num1" placeholder="Number 1"><br><br>')
        self.wfile.write(b'<input type="number" name="num2" placeholder="Number 2"><br><br>')
        self.wfile.write(b'<input type="radio" id="add" name="operation" value="add">')
        self.wfile.write(b'<label for="add">Add</label><br>')
        self.wfile.write(b'<input type="radio" id="subtract" name="operation" value="subtract">')
        self.wfile.write(b'<label for="subtract">Subtract</label><br>')
        self.wfile.write(b'<input type="radio" id="multiply" name="operation" value="multiply">')
        self.wfile.write(b'<label for="multiply">Multiply</label><br>')
        self.wfile.write(b'<input type="radio" id="divide" name="operation" value="divide">')
        self.wfile.write(b'<label for="divide">Divide</label><br><br>')
        self.wfile.write(b'<input type="submit" value="Calculate">')
        self.wfile.write(b'</form>')
        self.wfile.write(b'</body></html>')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        import urllib.parse
        body = urllib.parse.parse_qs(body.decode('utf-8'))
        num1 = float(body.get('num1', [0])[0])
        num2 = float(body.get('num2', [0])[0])
        operation = body.get('operation', ['add'])[0]
        calculator = Calculator()
        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'subtract':
            result = calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator.divide(num1, num2)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Calculator Webpage</h1>')
        self.wfile.write(f'Result: {result}'.encode())
        self.wfile.write(b'</body></html>')


def run_server(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
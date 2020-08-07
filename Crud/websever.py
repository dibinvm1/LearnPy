from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class weServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if(self.path.endswith("/hello")):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Hello!</h1>"
            output += '''<form method='POST' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output.encode())
            print(output)
            return

        if (self.path.endswith("/hola")):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            message = "<html><body>&#161Hola! <a href='/hello'> Back to Hello </a></body</html>"
            self.wfile.write(message.encode())
            print(message)
            return
        else:
            self.send_error(404,"File Not found %s"%self.path)
            return
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text\html')
        self.end_headers()
        length = int(self.headers.get('Content-Length',0))
        data = self.rfile.read(length).decode()
        messagecontent = parse_qs(data).get('message',None)[0] 
        output = ""
        output += "<html><body>"
        output += " <h2> Okay, how about this: </h2>"
        output += "<h1> %s </h1>" % messagecontent
        output += '''<form method='POST' action='/hello'><h2>What else would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
        output += "</body></html>"
        self.wfile.write(output.encode())
        print(output)
        
def main():
    try:
        port = 8080
        server = HTTPServer(('',port),weServerHandler)
        print("Sever runing on port {}".format(port))
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered Stopiing the Web Server")
        server.socket.close()

if __name__ == '__main__':
    main()
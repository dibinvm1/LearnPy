from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs , urlparse , quote
from db_functions import getAllRestaurentNames ,addRestaurantToDB , renameRestaurantInDB , deleteRestaurantFromDB ,getNameFromId
import bleach

class weServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if(self.path.endswith("/restaurants/new")):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            output = ""
            output += '''<form method='POST' action='/restaurants/new?q=add'><h2>Add a New Restaurant to The List!</h2><input name="message" type="text" ><input type="submit" value="ADD"> </form>'''
            self.wfile.write(output.encode())
            #print(output)
            return
        if(urlparse(self.path).path == '/restaurants/edit'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            try :
                r_id = int(parse_qs(urlparse(self.path).query).get('id',None)[0])
            except TypeError:
                pass
            restName = getNameFromId(r_id)
            output = ""
            output += '''<form method='POST' action='/restaurants/edit?q=edit&id={0}'><h2>{1}</h2><input name="message" type="text" ><input type="submit" value="Rename"> </form>'''.format(r_id,restName)
            self.wfile.write(output.encode())
            #print(output)
            return
        if(urlparse(self.path).path == '/restaurants/delete'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            try :
                r_id = int(parse_qs(urlparse(self.path).query).get('id',None)[0])
            except TypeError:
                pass
            restName = getNameFromId(r_id)
            output = ""
            output += '''<form method='POST' action='/restaurants/delete?q=delete&id={0}'><h2>Are you sure you want to Delete {1} from the list</h2><input type="submit" value="DELETE"> </form>'''.format(r_id,restName)
            self.wfile.write(output.encode())
            #print(output)
            return
        if(self.path.endswith("/restaurants")):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Restaurants List</h1>"
            rinfos = getAllRestaurentNames()
            for rinfo in rinfos:
                output += "<h3>"
                output += str(rinfo[1])
                output += "</h2><a href='/restaurants/edit?id={0}'style='display:inline-block; margin-right:10px;'><h3>Edit</h3> </a> <a href='/restaurants/delete?id={0}' style='display:inline-block;'><h3>Delete</h3></a>".format(rinfo[0])
            output += "<a href='/restaurants/new'> <h2> Add New Restaurant</h2> </a> "
            output += "</body></html>"
            self.wfile.write(output.encode())
            #print(output)
            return
        else:
            print(urlparse(self.path).path)
            self.send_error(404,"File Not found %s"%self.path)
            return
    
    def do_POST(self):
        try:
            length = int(self.headers.get('Content-Length',0))
            data = self.rfile.read(length).decode()

            urlParsed = urlparse(self.path)
            whatToDo = parse_qs(urlParsed.query).get('q',None)[0]
            
            if(whatToDo == 'add'):
                restName = parse_qs(data).get('message',None)[0]
                addRestaurantToDB(restName)
            
            elif (whatToDo == 'edit'):
                r_id = parse_qs(urlParsed.query).get('id',None)[0]
                newName = parse_qs(data).get('message',None)[0]
                renameRestaurantInDB(r_id,newName)
            
            elif (whatToDo == "delete"):
                r_id = parse_qs(urlParsed.query).get('id',None)[0]
                deleteRestaurantFromDB(r_id)
        except TypeError:
            self.send_error(400,"Request Can Not be Empty")
            return
        self.send_response(301)
        self.send_header('Location','/restaurants')
        self.end_headers()
        
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
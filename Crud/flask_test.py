from flask import Flask
from db_functions import getAllRestaurentNames

app = Flask(__name__)

@app.route('/')
@app.route('/hello')

def HelloWorld():
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
    return output

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0' , port= 5000)
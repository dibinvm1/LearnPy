from flask import Flask
from db_functions import getAllMenuItems,getAllMenuItemsByRestaurentId

app = Flask(__name__)

@app.route('/')
@app.route('/hello')

def HelloWorld():
    output = ""
    output += "<html><body>"
    output += "<h1>Menu Items</h1>"
    menuinfos = getAllMenuItems()
    for menuinfo in menuinfos:
        output += "<h3>"
        output += menuinfo[0]
        output += "</h3>"
        output += "<h3>"
        output += menuinfo[1]
        output += "</h3>"
        output += "<h3>"
        output += menuinfo[2]
        output += "</h3></br>"
    output += "</body></html>"
    return output

@app.route('/restaurants/<int:restaurant_id>/')
def restaurentMenu(restaurant_id):
    items = getAllMenuItemsByRestaurentId(restaurant_id)
    output = ""
    output += "<html><body>"
    for item in items:
        output += "<h3>"
        output += item[0]
        output += "</h3>"
        output += "<h3>"
        output += item[1]
        output += "</h3>"
        output += "<h3>"
        output += item[2]
        output += "</h3></br>"
    output += "</body></html>"
    return output


if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0' , port= 5000)
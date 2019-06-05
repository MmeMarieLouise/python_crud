# import the Flask (capitalised) class
from flask import Flask
# import request - global object
from flask import request

# create the class instance , app / instantiate the class
# pass in 'dunder' (double underscore) name, this is the namespace variable
# use whatever the current namespace is
app = Flask(__name__)

# route decorator (function) creates a view
# specify the route with ('/')
@app.route('/')
# index function defines the route
def index():
    return ''


# there are multiple routes to allow the app to respond on multiple end points
# make a request using HTTP 'POST' method to create file at specified path
@app.route('/create', methods=['POST'])
def create():
    # name response object 'received_data', store JSON within it
    received_data = request.get_json()
    path_key = received_data['path']
    name_key = received_data['name']
    contents = received_data['contents']
    write_file(path_key, name_key,contents)
    return 'File created'

# make a request using HTTP 'GET' method to read file at specified path
@app.route('/read', methods=['GET'])
def read():
    received_data = request.get_json()
    path_key = received_data['path']
    name_key = received_data['name']
    file_object = open(path_key +"/"+ name_key, "r")
    read_content = file_object.read()
    file_object.close()
    return read_content

# create update request
@app.route('/update', methods=['POST'])
def update():
    received_data = request.get_json()
    name_key = received_data['name']
    path_key = received_data['path']
    contents = received_data['contents']
    # todo: only update file if it exists
    write_file(path_key, name_key,contents)
    return 'File updated'

def write_file(path, name, contents):
    myFile = open( path + "/" + name, "w+")
    myFile.write(contents)
    myFile.close()

# delete file
#@app.route('/delete', methods=['POST'])
#def delete_file():
   #return ''

# run the app
# debug = true , so that Flask will auto re-start anytime changes are made
app.run(debug=True)

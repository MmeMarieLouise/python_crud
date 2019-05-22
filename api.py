from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/create', methods=['POST'])
def create():
    received_data = request.get_json()
    path_key = received_data['path']
    name_key = received_data['name']
    myFile = open( path_key + "/" + name_key, "w+")
    myFile.write(received_data['contents'])
    myFile.close()
    return 'file created'


@app.route('/read', methods=['GET'])
def read():
    received_data = request.get_json()
    path_key = received_data['path']
    name_key = received_data['name']
    file_object = open(path_key +"/"+ name_key, "r")
    read_content = file_object.read()
    file_object.close()
    return read_content

app.run(debug=True)

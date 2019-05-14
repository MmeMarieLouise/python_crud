from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/create', methods = ['POST'])
def create():
    received_data = request.get_json()
    # get data from request
    # myFile = open("new", "w+")
    # write hello to test-file
    return 'file created'


app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/create', methods = ['POST'])
def create():
    return 'file created'


app.run(debug=True)

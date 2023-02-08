from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
    return "<h1> Hello,world</h1>"

@app.route('/index')
@app.route('/home')

def home():
    return "<h1> home page! </h1>"
    

if __name__ == "__main__":
    app.run()
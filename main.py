from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
    return "<h1> Hello,world</h1>"

@app.route('/index')
@app.route('/home')

def home():
    return "<h1> home page! </h1>"

@app.route("/salom")
def salom():
    return "<h1> Salom  </h1>"

@app.route("/about")
def about():
    return "<h1> Abaout page  </h1>"

if __name__ == "__main__":
    app.run()
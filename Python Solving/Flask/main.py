from flask import Flask, render_template
'''It creates an instance of a flask class, 
which will be your WSGI (Web Server Gateway Interface) applicaation'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course. This should be an amazing course. This is the best course and in this course you will learn about the flask framework"

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
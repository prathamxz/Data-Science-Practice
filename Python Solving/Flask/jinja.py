#Building URl dynamically
#Variable rule
# Jinja 2 template engine
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Variable rule
@app.route ('/success/<int:score>')
def success(score):
    res = ""
    if score >=50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result.html',results = res)
     


if __name__ == '__main__':
    app.run(debug=True)
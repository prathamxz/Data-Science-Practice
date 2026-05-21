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
     
@app.route ('/successres/<int:score>')
def successres(score):
    res = ""
    if score >=50:
        res = "Passed"
    else:
        res = "Failed"
    
    exp = {'score': score,"res":res}

    return render_template('result1.html',results = exp)
     



if __name__ == '__main__':
    app.run(debug=True)
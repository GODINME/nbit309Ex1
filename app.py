from flask import Flask, render_template

app = Flask(__name__, template_folder="")

@app.route('/')
def app_started():
    return render_template('app.html')

@app.route('/hello')
def hello():
    return "Hello Customers!!!"
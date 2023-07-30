from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def app_started():
    return render_template('app.html')

@app.route('/hello')
def hello():
    return "Hello Customers!!!"

@app.route('/main')
def main_page():
    return render_template("main.html")

@app.route('/service')
def service_page():
    return render_template("service.html")
from flask import Flask

app = Flask('__name__')

@app.route('/')
def app_started():
    return "App Started...!!!"
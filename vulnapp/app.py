from flask import Flask, abort, render_template, redirect, request, url_for
import requests
from os import path, environ

DEADLINE = 6

app = Flask(__name__)
app._static_folder = path.abspath('static/')

@app.errorhandler(403)
def forbbiden(e):
    return render_template('error.html', error=str(e)), 403

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', error=str(e)), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

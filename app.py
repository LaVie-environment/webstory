#!/usr/bin/env python3

# let's import the flask
from flask import Flask, 
render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = 'Cloud Engineering Acts'
    return render_template('home.html', name = name, tech=techs, title = 'Home')

@app.route('/about')
def about():
    name = 'Cloud Engineering Acts'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name = name, title = name)

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
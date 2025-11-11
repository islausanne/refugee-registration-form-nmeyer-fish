from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register')
def register():
    name = request.form['name']
    email = request.form['email']
    return f"Thank you, {name}. Your email address is {email}."


@app.route('/contact')
def contact():
    return "Contact us at: info@example.com."

if __name__ == '__main__':
    app.run(debug=True)




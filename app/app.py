#!/usr/local/bin/python3

from flask import Flask, render_template, request
from app.send_page import send_page


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', status='')

@app.route("/", methods=['POST'])
def send():
    result = send_page(
        name=request.form.get('name'),
        email=request.form.get('email'),
        message=request.form.get('message')
    )
    status = 'success' if result[0] else 'fail'
    return render_template('index.html', status=status)

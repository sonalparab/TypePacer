from flask import Flask, render_template, request
import requests, base64, json, os

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route('/', methods = ['GET','POST'])
def root():
    return


import pandas as pd
from flask import Flask, redirect, render_template, request, url_for, make_response

import os.path

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return "Test"

if  __name__ =="__main__":
    app.run(host='0.0.0.0', port='5010', debug=True)

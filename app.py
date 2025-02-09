import pandas as pd
from flask import Flask, redirect, render_template, request, url_for, make_response

import os.path

app = Flask(__name__, template_folder="templates")

if not os.path.exists('polls.csv'):
    structure={
        'id': [],
        'poll': [],
        'option1': [],
        'option2': [],
        'option3': [],
        'votes1': [],
        'votes2': [],
        'votes3': [],

    }

    pd.DataFrame(structure).set_index("id").to_csv("polls.csv")

polls_df = pd.read_csv("polls.csv").set_index("id")

@app.route('/')
def index():
    return "Test"

if  __name__ =="__main__":
    app.run(host='0.0.0.0', port='5010', debug=True)

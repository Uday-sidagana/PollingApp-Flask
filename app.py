import pandas as pd
from flask import Flask, redirect, render_template, request, url_for, make_response

import os.path

app = Flask(__name__, template_folder="templates")
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
import numpy as np
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(port=33507)
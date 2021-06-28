from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
import numpy as np
from bokeh.embed import components

# from stocks import stocks

# class StockForm(FlaskForm):
#   closing = BooleanField('Closing Price')
#   adjusted_closing = BooleanField('Adjusted Closing Price')
#   opening = BooleanField('Opening Price')
#   adjusted_opening = BooleanField('Adjusted Opening Price')
#   submit = SubmitField('Submit')


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess string'

# bootstrap = Bootstrap(app)

# # Pulling the stock data
# import pandas as pd
# from dotenv import load_dotenv
# import os

# load_dotenv()
# api_key = os.environ['19CLJ8KCICHV7QXL']
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey={}'.format(api_key)
# r = request.get(url)
# data = r.json()
# df = pd.DataFrame(data)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()

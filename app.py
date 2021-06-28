from flask import Flask, render_template, request, redirect
import numpy as np
from bokeh.embed import components
# Pulling the stock data
import pandas as pd
# from dotenv import load_dotenv
# import os

# load_dotenv()
# api_key = os.environ['19CLJ8KCICHV7QXL']
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey={}'.format(api_key)
# r = request.get(url)
# data = r.json()
# df = pd.DataFrame(data)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
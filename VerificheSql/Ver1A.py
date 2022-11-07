from flask import Flask, render_template, request, Response
app = Flask(__name__)

import io
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import pymssql



@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
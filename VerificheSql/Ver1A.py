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
    return render_template("home1A.html")


@app.route("/ricerca", methods=["GET"])
def ricerca():
    nomestore = request.args['store']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='dilecce.gabriele', password='xxx123##', database='dilecce.gabriele')
    query = f"SELECT sf.first_name, sf.last_name FROM sales.stores AS st INNER JOIN sales.staffs AS sf ON as.store_id = st.store_id WHERE st.store_name  '{nomestore}'"
    df= pd.read_sql
    if df.values.tolist() == []:
        return render_template("errore.html")
    else:
        return render_template("risultati1A.html", nomiColonne = df.columns.values, dati = list(df.values.tolist()))

    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
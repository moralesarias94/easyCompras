from flask import Flask, render_template, redirect, url_for
import pandas as pd
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/inicio')
def index():
    productos = requests.get(url).json()
    return render_template('reporte.html', productos = productos['_items'])


@app.route('/detalle/<nombre>', methods=['GET'])
def dashboard(cedula, agradecimiento=False):
    if(nombre):
        url = 'http://api-easy-compras.herokuapp.com/productos'
        params = {'where' : json.dumps({'nombre': nombre})}
        producto = requests.get(url, params=params).json()
        producto = producto['_items'][0]
        return render_template('cedula_dashboard.html', producto=producto)
    else:
        return render_template('empty_dashboard.html')

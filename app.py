from flask import Flask, render_template, redirect, url_for
import requests
import json
import numpy as np
app = Flask(__name__)

@app.template_global(name='zip')
def _zip(*args, **kwargs): #to not overwrite builtin zip in globals
    return zip(*args, **kwargs)

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/inicio', defaults={'nombre': None} ,methods=['GET'])
@app.route('/inicio/<nombre>',methods=['GET'])
def index(nombre):
    url = 'https://easycompras-api.herokuapp.com/productos'
    params = None    
    if(nombre):
        params = {'where' : json.dumps({'nombre': {"$regex": f".*{nombre.lower()}.*"}})}
    productos = requests.get(url, params=params).json()
    return render_template('index.html', productos = productos['_items'])

@app.route('/detalle/<nombre>', methods=['GET'])
def detail(nombre):
    url = 'https://easycompras-api.herokuapp.com/productos'
    params = {'where' : json.dumps({'nombre': nombre})}
    producto = requests.get(url, params=params).json()
    try:
        producto = producto['_items'][0]
        print(producto)
        proveedores = producto['proveedores']  
        precios = producto['precios']
        min_precio = np.argmin(precios)
        producto['precio'] = precios[min_precio]
        producto['proveedor_precio'] = proveedores[min_precio]
    except IndexError as e:
        producto = None
    return render_template('detail.html', producto=producto)
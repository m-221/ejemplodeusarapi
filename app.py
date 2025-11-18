from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import requests
app = Flask(__name__)
API_URL = 'https://api.spoonacular.com/recipes/findByIngredients'
API_KEY = '923b514b2c604404954302eaebfea6fd'  


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/resetas')
def rs():
    return render_template('reseta.html')


@app.route('/buscar', methods=['GET', 'POST'])
def buscar_recetas():
    recetas = []
    
    if request.method == 'POST':
        ingrediente = request.form.get('ingrediente')

        params = {
            'apiKey': API_KEY,
            'query': ingrediente,   
        }

        respuesta = requests.get(API_URL, params=params)
        data = respuesta.json()

        recetas = data.get('params', [])

    return render_template('recetas.html', recetas=recetas)

if __name__ == '__main__':
    app.run(debug=True)
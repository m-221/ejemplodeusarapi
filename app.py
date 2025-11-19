from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests

app = Flask(__name__)
app.secret_key = 'melyyyyaaasdwwd'

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
        if ingrediente:
            params = {
                'apiKey': API_KEY,
                'ingredients': ingrediente, 
                'number': 10,                 
                'ranking': 1            
            }

            respuesta = requests.get(API_URL, params=params)
            
        
            if respuesta.status_code == 200:
                recetas = respuesta.json()

            else:
                flash('Error al obtener las recetas. Intenta de nuevo más tarde.', 'error')
                return render_template('inicio.html')
        else:
            flash('Por favor, ingresa un ingrediente para buscar.', 'error')
            return render_template('inicio.html')

    return render_template('receta.html', recetas=recetas)

if __name__ == '__main__':
    app.run(debug=True)

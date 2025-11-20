from flask import Flask, jsonify, request, url_for, redirect, render_template
import requests

app = Flask(__name__)
app.secret_key = 'tumelyKEY1904'

API_KEY = '923b514b2c604404954302eaebfea6fd'
API_URL = 'https://api.spoonacular.com/recipes/findByIngredients'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resultado')
def resu():
    return render_template('resultado.html')


@app.route('/buscar')
def buscar():
    ingredientes = request.args.get("ingredientes")

    if not ingredientes:
        return render_template("resultado.html", error="Debes escribir al menos un ingrediente.")

    params = {
        "ingredients": ingredientes,
        "number": 10,
        "apiKey": API_KEY
    }

    respuesta = requests.get(API_URL, params=params)

    if respuesta.status_code != 200:
        return render_template("resultado.html", error="Error al consultar Spoonacular. Intenta más tarde.")

    recetas = respuesta.json()

    for receta in recetas:
        receta["ingredientes_usados"] = [
            f"{ing.get('name')} ({ing.get('amount', 0)} {ing.get('unit', '')})".strip()
            for ing in receta.get("usedIngredients", [])
        ]

    return render_template(
        "resultado.html",
        ingredientes=ingredientes,
        recetas=recetas
    )





if __name__  == '__main__':
    app.run(debug=True)
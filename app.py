from flask import Flask, render_template, request, redirect, url_for, flash
import requests

API = "https://api.spoonacular.com/recipes/findByIngredients"
app = Flask(__name__)
app.secret_key = 'claVe_SeCReTa_My_ClAvE'


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/resetas')
def rs():
    return render_template('reseta.html')




@app.route('/search', methods=['POST'])
def search_resetas():
    resetas = request.form.get('reseta', '').strip().lower()  

    if not resetas:
        flash('Por favor, ingresa bien la información', 'error')
        return redirect(url_for('index'))

    try:
        respuesta = requests.get(f"{API}{resetas}")
        if respuesta.status_code == 200:
            resetas_data = respuesta.json()
            formatted_data = format_resetas_data(resetas_data)
            return render_template('reseta.html', resetas=formatted_data)
        else:
            flash('reseta no encontrado. Por favor, intenta de nuevo.', 'error')
            return redirect(url_for('rs'))

    except requests.exceptions.RequestException:
        flash('Error al conectar con la API. Por favor, intenta de nuevo más tarde.', 'error')
        return redirect(url_for('index'))


def format_resetas_data(resetas_data):
    return 







if __name__ == '__main__':
    app.run(debug=True)
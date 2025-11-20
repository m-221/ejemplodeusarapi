from flask import Flask, jsonify, request,url_for,redirect,render_template
import requests
app = Flask(__name__)
app.secret_key = 'tumelyKEY1904'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recetas')
def buscar_recetas():
    return  render_template('recetas.html')

@app.route('/buscar')
def buscar():
     return







if __name__  == '__main__':
       app.run(debug=True)
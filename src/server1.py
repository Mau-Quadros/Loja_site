from flask import Flask,render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/registrar")
def regitro():
    return render_template('registro.html')

@app.route("/cadastrado")
def registrado():
    return render_template('cadastrado.html')



if __name__ == '__main__':
    app.run()

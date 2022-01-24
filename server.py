from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key='infoconfidencial'

@app.route('/' , methods=['GET'])
def paginaPrincipal():
     return render_template('index.html')

@app.route('/result',methods=['GET'])
def paginaRegistro():
     return render_template('plataforma.html')
 

@app.route('/registro', methods=['POST'])
def Registro():
     session["nombre"] = request.form["nombre"]
     session ["lugar"] = request.form["lugar"]
     session["lenguaje"] = request.form["lenguaje"]
     session["comentario"] = request.form["comentario"]
     return redirect('/result')

@app.route('/salir', methods=['GET'])
def Salir():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
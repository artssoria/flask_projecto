# primero hay que hacer la instalacion de los paquetes de python
'''
primero hay que crear el archivo hay que crear la carpeta donde aloja el documento, ejemplo "proyecto-flask", ingresamos a la carpeta, despues abrimos la terminal en esa carpeta ya sea por git bash o cmd. Despues dentro ejecutamos "python -m venv env" enter y esperamos a que se cree la carpeta (env), despues debemos activar ese entorno virtual.
ya sea activandolo con cd env/scripts/activate o si estamos en gitbash mediante source env/bin/activate
luego hay que instalar las dependencias dentro de un archivo txt llamado requeriments.txt
el mismo debe contener los paquetes Flask, SQLALchemy y Flask-SQLAlchemy 
para ejecutarlo ya con la terminal y el entorno activo debemos utilizar el comando
pip install -r requirements.txt y enter 
una vez instalado debemos crear nuestro primer archivo llamado app.py 
'''

import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuración de la URI de la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'blog.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime, default=datetime.now)
	texto = db.Column(db.String, nullable=False)
 
@app.route("/")
def inicio():
    posts = Post.query.order_by(Post.fecha.desc()).all()
    return render_template("inicio.html", posts=posts)

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")
@app.route("/crear", methods=["POST"])
def crear_post():
	titulo = request.form.get("titulo")
	texto = request.form.get("texto")
	post = Post(titulo=titulo, texto=texto)
	db.session.add(post)
	db.session.commit()
	return redirect("/")

@app.route("/borrar", methods=["POST"])
def borrar():
	post_id = request.form.get("post_id")
	post = db.session.query(Post).filter(Post.id==post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect("/")
    
if __name__ == '__main__':
    app.run(debug=True)
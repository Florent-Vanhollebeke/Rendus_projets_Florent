from flask import Flask, render_template, request
import mysql.connector as mariadb
import os
import pandas as pd
from werkzeug.utils import secure_filename

#from dotenv import load_dotenv
#load_dotenv()
#user = os.environ.get('user')
#password = os.environ.get('password')


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "data/"

#Connexion à la base MariaDB
#mdbusr = os.getenv('mariadb_usr')
#mdbpwd = os.getenv('mariadb_pwd') 
conn = mariadb.connect(host='localhost', user='root', password="PASSWORD A REMETTRE")
curseur = conn.cursor()
curseur.execute("CREATE DATABASE IF NOT EXISTS projet_flask")
curseur.execute("USE users")
curseur.execute("CREATE TABLE IF NOT EXISTS users (prenom VARCHAR(20), nom VARCHAR(20), sexe VARCHAR(10), pseudo VARCHAR(20) UNIQUE)")

@app.route('/')
def hello():
    return render_template("home.html", message='Hello World!')

@app.route('/page2')
def suite():
    return render_template("page2.html")

@app.route('/test-formulaire')
def enregistrement():
    return render_template("formulaire.html")

@app.route('/retour-formulaire', methods=['POST'])
def text_box():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    sex = request.form['sex']
    pseudo = request.form['pseudo']
    curseur = conn.cursor()
    curseur.execute("INSERT INTO users VALUES ('{}','{}','{}','{}')".format(first_name,last_name,sex,pseudo))
    conn.commit()
    return render_template("bienvenue.html",first_name=first_name,last_name=last_name, sex=sex, pseudo=pseudo)

@app.route('/users', methods=['GET'])
def users():
    curseur = conn.cursor()
    curseur.execute("SELECT prenom,nom,sexe,pseudo FROM users")
    res = curseur.fetchall()
    conn.commit()
    return render_template("users.html", res = res)

@app.route('/upload')
def upload_file():
    return render_template("data.html")

@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = pd.read_csv(file).describe()   
        
    return render_template('content.html', content=content) 

if __name__ == "__main__":
    app.run(debug=True)
    
    
  
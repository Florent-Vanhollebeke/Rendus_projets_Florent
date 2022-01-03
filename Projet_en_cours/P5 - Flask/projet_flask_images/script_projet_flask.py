from flask import Flask, render_template, request
import mysql.connector as mariadb
import os
import pandas as pd
from werkzeug.utils import secure_filename

#import spécifique à la partie MNIST
import pickle
import base64
import cv2 
import numpy as np
from scipy import ndimage


#from dotenv import load_dotenv
#load_dotenv()
#user = os.environ.get('user')
#password = os.environ.get('password')


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "data/"



#Connexion à la base MariaDB
#mdbusr = os.getenv('mariadb_usr')
#mdbpwd = os.getenv('mariadb_pwd') 
conn = mariadb.connect(host='localhost', user='root', password="password")
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
    curseur.execute("SELECT * FROM users")
    liste_users = list()
    for user in curseur:
        liste_users.append(user)
    conn.commit()
    return render_template("users.html", liste_users=liste_users)

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


model = pickle.load(open('mnist.sav', 'rb'))

@app.route("/mnist")
def mnist():
    return render_template("mnist.html")

#récupération de l'image et prédiction
@app.route('/dataurl', methods=['POST'])
def predict_from_dataurl():
    #récupération des données de l'image depuis l'URL base64
    imgstring = request.form.get('data')

    #conversion en array de pixels grayscale
    encoded_data = imgstring.split(',')[1]
    arr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

    #conversion array 140*140 en array 28*28 en moyennant les pixels par groupe de 5*5 
    img = img.reshape(28,5,28,5).mean(-1).mean(1)

    #récupération du centre de masse de l'image pour la décaler et la recentrer
    cy, cx = ndimage.measurements.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]]) #matrice de transformation pour une translation
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    #prédiction
    pred = model.predict(img.reshape(1,-1))[0]

    return str(pred)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request, session, url_for
#from requests import session
from src.utils import *
from acces_azure import *
import cv2
from base64 import b64encode
from PIL import Image
import numpy as np
from io import BytesIO

import os
import random
from matplotlib.image import imread

from script_clean_or_dirty import *


app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():
    open_waste_slot()
    paths = os.listdir('test')
    path = random.choice(paths)
    pics = take_trash_picture(path)
    pred = first_prediction_azure('test/'+path)
    session['solution'] = pred
    PIL_image = Image.fromarray(np.uint8(pics)).convert('RGB')
    PIL_image2 = PIL_image.resize((256,256))
    PIL_image2.save("{PIL_image}.jpg", "JPEG", optimize=True)
    data = BytesIO()
    PIL_image2.save(data, "JPEG")
    data64 = b64encode(data.getvalue())
    PIL_image2 = u'data:img/jpeg;base64,'+data64.decode('utf-8') 
    return render_template('insert.html', pics = PIL_image2, prediction = pred)


@app.route('/waste/pick-type')
def pick_type():
    close_waste_slot()
    message = session.get('solution')

    return render_template('type.html',message=message)


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')





@app.route('/propre')
def clean_dirty():
    open_waste_slot()
    paths = os.listdir('test')
    path = random.choice(paths)
    pics = take_trash_picture(path)
    pred = clean_or_dirty('test/'+path)
    session['solution'] = pred
    PIL_image = Image.fromarray(np.uint8(pics)).convert('RGB')
    PIL_image2 = PIL_image.resize((256,256))
    PIL_image2.save("{PIL_image}.jpg", "JPEG", optimize=True)
    data = BytesIO()
    PIL_image2.save(data, "JPEG")
    data64 = b64encode(data.getvalue())
    PIL_image2 = u'data:img/jpeg;base64,'+data64.decode('utf-8') 
    return render_template('resultat.html', pics = PIL_image2, prediction = pred)


@app.route('/suite')
def suite_proprete():
    close_waste_slot()
    message = session.get('solution')

    return render_template('proprete.html',message=message)

@app.route('/remerciement', methods=['POST'])
def remerciement():
    waste_type = request.form['proprete']

    process_waste(waste_type)
    return render_template('confirmation.html')





if __name__ == "__main__":
    app.run(debug=True)

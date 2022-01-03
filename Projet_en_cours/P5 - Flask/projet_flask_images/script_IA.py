import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import keras
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from keras.datasets import mnist
import pickle


(X_train, y_train), (X_test, y_test) = mnist.load_data()

def afficher_images(nb_images_a_afficher, nb_colonnes=5):
    nb_lignes = nb_images_a_afficher//nb_colonnes+1
    plt.figure(figsize=(20,5*nb_lignes))
    for index, (image, label) in enumerate(zip(X_train[0:nb_images_a_afficher], y_train[0:nb_images_a_afficher])):
        plt.subplot(nb_lignes, nb_colonnes, index + 1)
        plt.imshow(image)
        plt.title('Training: %i\n' % label, fontsize = 15)
afficher_images(15)


# reshape des images en vecteur
X_train = X_train.reshape(60000,-1)
X_test = X_test.reshape(10000,-1)

model = RandomForestClassifier(n_estimators=500, max_features=50, n_jobs=3)
model.fit(X_train, y_train)
model.score(X_test,y_test)
#y_pred = reglog.predict(X_test)

pickle.dump(model, open('mnist.sav', 'wb'))

# la suite servira au chargement (désérialisation) de l'objet python (le modèle IA) précédemment sérialisé  
# with open('picklefile', 'rb') as f1:
#    model = pickle.load(f1)

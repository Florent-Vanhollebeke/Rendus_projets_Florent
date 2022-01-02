import numpy as np 
import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from keras.datasets import mnist
import pickle


(X_train, y_train), (X_test, y_test) = mnist.load_data()

#division par 255 pour avoir des valeurs entre 0 et 1
X_train = X_train.reshape(X_train.shape[0],-1)/255 
X_test = X_test.reshape(X_test.shape[0],-1)/255

model = LogisticRegression(solver='lbfgs', max_iter=1000, n_jobs=8)
model.fit(X_train, y_train)
#y_pred = reglog.predict(X_test)

pickle.dump(model, open('mnist.sav', 'wb'))

# la suite servira au chargement (désérialisation) de l'objet python (le modèle IA) précédemment sérialisé  
# with open('picklefile', 'rb') as f1:
#    model = pickle.load(f1)

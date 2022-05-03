
import numpy as np
#import tensorflow 
#from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image

model = load_model('./my_model.h5')

def new_prediction(path):
    test_image = image.load_img(path, target_size = (150, 150))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    #training_set.class_indices

    if result[0][0] == 1:
        return 'dirty'  
    else:
        return 'clean'

def clean_or_dirty(path):
    res = new_prediction(path)
    return res


from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid


#path = "test/test_bouteille.jpg"

def first_prediction_azure(path):


    ENDPOINT = ""
    training_key = ""
    prediction_key = ""
    prediction_resource_id = ""


    base_image_location = ""
    publish_iteration_name = "model1"
    project_id=""


    # Test du point de terminaison
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


    resultat = ""

    with open(os.path.join (base_image_location, path), "rb") as image_contents:
        results = predictor.classify_image(
            project_id, publish_iteration_name, image_contents.read())

        for prediction in results.predictions:
        #print("\t" + prediction.tag_name +
             # ": {0:.2f}%".format(prediction.probability * 100))
            if (results.predictions[0].probability > results.predictions[1].probability) or (results.predictions[0].probability > results.predictions[2].probability):
                resultat = results.predictions[0].tag_name
            elif results.predictions[1].probability > results.predictions[0].probability or (results.predictions[1].probability > results.predictions[2].probability):
                resultat = results.predictions[1].tag_name
            else:
                resultat = results.predictions[2].tag_name

    return resultat



#first_prediction_azure(path)


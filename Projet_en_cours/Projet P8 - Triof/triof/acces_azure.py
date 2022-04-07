from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid


#path = "test/test_bouteille.jpg"

def first_prediction_azure(path):


    ENDPOINT = "https://projetp8custom-prediction.cognitiveservices.azure.com/"
    training_key = "88a6c3b9bdd14faabd2e7f98f3c65a49"
    prediction_key = "4ed5495ce8af4755a3487b2ba8dbef77"
    prediction_resource_id = "/subscriptions/9b9c4a7a-4f40-4fc2-ab99-0bbe0c4064bd/resourceGroups/Florent-IA/providers/Microsoft.CognitiveServices/accounts/projetP8custom"


    base_image_location = "/Users/flore/OneDrive/Documents/Simplon/Rendus_projets_Florent/Projet_en_cours/Projet P8 - Triof/triof"
    # base_image_location = "base_image_location = "/mnt/c/Documents and Settings/flore/OneDrive/Documents/Simplon/Rendus_projets_Florent/Projet_en_cours/Projet P8 - Triof/triof/"
    publish_iteration_name = "model1"
    project_id="66b07b7d-03ff-4c7e-9892-9d854e949ad0"


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


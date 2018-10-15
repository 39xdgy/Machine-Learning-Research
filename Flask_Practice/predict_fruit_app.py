import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
import tensorflow as tf
import re


app = Flask(__name__)

def get_model():
    global model
    global graph
    graph = tf.get_default_graph()
    model = load_model('neural_network.h5')
    print("Loaded model!")

def preprocess_image(image, target_size):
    if(image.mode) != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    print('-'*80)
    print(image)
    print('-' * 80)

    return image
print("Loading Keras model")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = re.sub('^data:image/.+;base64,', '', message['image'])
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(150, 150))

    with graph.as_default():
        prediction = model.predict(processed_image)

    response = {
        'prediction' : {
            'apple' : float(prediction[0][0]),
            'banana' : float(prediction[0][1]),
            'pear' : float(prediction[0][2])
        }
    }

    return jsonify(response)

app.run()
from fastapi import FastAPI, File, UploadFile
import os
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import numpy as np
from flask import Flask, jsonify, render_template, request
import pickle

app = Flask(__name__)
MODEL = tf.keras.models.load_model("saved_models/1")
CLASS_NAMES = ['Early Blight', 'Healthy', 'Late Blight']


@app.route('/test',methods=['GET'])
def test():
    return "Test request received successfully. Service is running."


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    #f = request.files['file']
    print('Request')
    f = request.files['imagefile']
    filename = f.filename
    file_path = os.path.join('static/images', filename)
    f.save(file_path)
    i = tf.keras.preprocessing.image.load_img(file_path)
    inputArr = tf.keras.preprocessing.image.img_to_array(i)
    inputArr = np.expand_dims(inputArr,axis=0)
    #print(inputArr.shape)
    #print(inputArr)
    prediction = MODEL.predict(inputArr)
    predictionClass = CLASS_NAMES[np.argmax(prediction[0])]
    print(predictionClass)

    #return render_template('index.html', predicted_cls="LEAF CONDITION: {}".format(predictionClass))
    return predictionClass
    #print(file_path)
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
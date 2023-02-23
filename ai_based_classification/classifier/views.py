from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
import keras.utils as image
import tensorflow.compat.v1 as tf
import json
import numpy as np
from tensorflow.compat.v1 import Graph, Session
tf.disable_v2_behavior()




with open('./models/labels.json','r') as f:
    labels=f.read()
labels=json.loads(labels)

modelGraph = Graph()
with modelGraph.as_default():
    tf_session = Session()
    with tf_session.as_default():
        model=load_model('./models/mobileNet.h5')


def homePage(request):
    return render(request,'main.html')


def classify(request):

    

  
    

    imgPath = request.FILES['image']
    

    f = FileSystemStorage()

    imgPath = f.save(imgPath.name,imgPath)
    imgPath = f.url(imgPath)


    img = image.load_img('.'+imgPath, target_size=(224, 224))
    x_test = image.img_to_array(img)
    x_test=x_test/255
    x_test=x_test.reshape(1,224, 224,3)
    with modelGraph.as_default():
        with tf_session.as_default():
            y_pred=model.predict(x_test)

    prediction=labels[str(np.argmax(y_pred[0]))]
    
    return render(request,'main.html', {'img':imgPath,'prediction':prediction[1]})


    

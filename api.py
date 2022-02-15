import os
from fastai.vision.all import *
from flask import Flask, render_template, request

app = Flask(__name__) #Initialize the Flask app

UPLOAD_FOLDER = '/Users/goceovoono/Desktop/flask-app/static'
MODEL_FOLDER = '/Users/goceovoono/Desktop/flask-app/model-pretrained/'

#We have to define a label function for our model inference 
def is_cat(x): return x[0].isupper()

### Model inference
learn_inf = load_learner('/Users/goceovoono/Desktop/flask-app/model-pretrained/cat-dog-classifier.pkl', cpu = True)



### FLASK API
@app.route("/", methods= ['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file is not None:
            image_location = os.path.join(UPLOAD_FOLDER, image_file.filename)
            image_file.save(image_location)
            pred = f'{learn_inf.predict(image_location)[2][0]:.04f}'
            return render_template('index.html', prediction = pred, image_loc = image_file.filename)
    return render_template('index.html', prediction = 0, image_loc = None) 
if __name__ == '__main__':
    app.run(port = 12000, debug = True)
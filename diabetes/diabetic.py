from flask import Blueprint, render_template, request,url_for
import numpy as np
import pickle as pk


diabetic = Blueprint('diabetic',__name__)#, static_folder="static", template_folder="templates")

filename = 'models/diabetic_trained_model.pkl'
classifier = pk.load(open(filename,'rb'))
std = np.load('models/diabetes_std.npy')
mean = np.load('models/diabetes_mean.npy')

@diabetic.route('/', methods=['GET','POST'])
def diabetic_home():
    return render_template('diabetes.html')

@diabetic.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        data = (data-mean)/std
        my_prediction = classifier.predict(data)
        
        return render_template('diabetes.html', prediction=my_prediction)
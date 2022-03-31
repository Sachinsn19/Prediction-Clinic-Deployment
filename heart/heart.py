from flask import Blueprint, render_template, request
import numpy as np
import pickle as pk

heart = Blueprint('heart', __name__)

filename = "models/heart_disease_prediction_model.pkl"
classifier = pk.load(open(filename, "rb"))
std = np.load('models/heart_disease_std.npy')
mean = np.load('models/heart_disease_mean.npy')

@heart.route('/', methods=['GET','POST'])
def heart_disease_home():
    return render_template('heart_disease.html')

@heart.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Sex = int(request.form['Sex'])
        ChestPainType = int(request.form['ChestPainType'])
        RestingBP = int(request.form['RestingBP'])
        Cholesterol = int(request.form['Cholesterol'])
        FastingBS = int(request.form['FastingBS'])
        RestingECG = int(request.form['RestingECG'])
        MaxHR = int(request.form['MaxHR'])
        ExerciseAngina = int(request.form['ExerciseAngina'])
        Oldpeak = float(request.form['Oldpeak'])
        ST_Slope = int(request.form['ST_Slope'])
        data = np.array([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
        data = (data-mean)/std
        myprediction = classifier.predict(data)
        return render_template('heart_disease.html', prediction = myprediction)

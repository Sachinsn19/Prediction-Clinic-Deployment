from flask import Blueprint, render_template, request
import numpy as np
import pickle as pk

insurance = Blueprint('insurance', __name__)

filename = "models/medical_insurance_prediction_model.pkl"
regressor = pk.load(open(filename, 'rb'))

@insurance.route('/', methods=['GET','POST'])
def insurance_home():
    return render_template('insurance.html')

@insurance.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':  
        sex = int(request.form['sex'])
        region = int(request.form['region'])
        smoker = int(request.form['smoker'])
        age = int(request.form['age'])
        children = int(request.form['children'])
        bmi = float(request.form['bmi'])
        data = np.array([[age, sex, bmi, children, smoker, region]])
        myprediction = np.round(regressor.predict(data)[0],2)
        return render_template('insurance.html', prediction = myprediction)



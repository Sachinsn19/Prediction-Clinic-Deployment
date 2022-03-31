from flask import Blueprint, render_template, request
import numpy as np
import pickle as pk



cancer = Blueprint('cancer',__name__)

filename = "models/breast_cancer_trained_model.pkl"
classifier = pk.load(open(filename,'rb'))
std = np.load('models/breast_cancer_std.npy')
mean = np.load('models/breast_cancer_mean.npy')

@cancer.route('/',methods=['GET','POST'])
def breastCancer():
    return render_template('breast_cancer.html')

@cancer.route('/predict', methods=['GET','POST'])
def cancer_predict():
    if request.method=='POST':
        parameters = ['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean',
        'compactness_mean','concavity_mean','concave_points_mean','symmetry_mean','fractal_dimension_mean',
        'radius_se','texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se',
        'concave_points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst',
        'perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst',
        'concave_points_worst','symmetry_worst','fractal_dimension_worst']
        argument_list = []
        for params in parameters:
            params = float(request.form[params])
            argument_list.append(params)
        data = [argument_list]
        data = (data-mean)/std
        myprediction = classifier.predict(data)
        

        myprediction = classifier.predict(data)[0]
        return render_template('breast_cancer.html', prediction= myprediction )
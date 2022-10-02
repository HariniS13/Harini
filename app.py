from array import array 
from distutils.log import debug 
import pickle 
import numpy as np 
from flask import Flask, render_template, request 
app = Flask(_name_, template_folder='template') 
model = pickle.load(open('model.pkl','rb')) 
def city(): 
    try: 
        float(request.form.get('city'))
    except: 
        print('Not a number')  
def dateobj(): 
    try: 
        request.form.get('date') 
    except: 
        print('Invalid')            
def street(): 
    try: 
        request.form.get('street') 
    except: 
        print('Invalid') 
def statezip(): 
    try:
        request.form.get('statezip') 
    except: 
        print('Invalid') 
def country(): 
    try:
        request.form.get('country') 
    except: 
        print('Invalid') 
@app.route('/') 
def index(): 
    return render_template('index.html') 
    @app.route('/predict',methods=['GET','POST']) 
def predict(): 
    arr=[] 
    l=[] 
    l.append(float(request.form.get('bedrooms'))) 
    l.append(float(request.form.get('bathrooms'))) 
    l.append(float(request.form.get('sqft_living'))) 
    l.append(float(request.form.get('sqft_lot'))) 
    l.append(request.form.get('floors')) 
    l.append(dateobj()) 
    l.append(request.form.get('waterfront')) 
    l.append(request.form.get('view')) 
    l.append(request.form.get('condition')) 
    l.append(request.form.get('sqft_above')) 
    l.append(request.form.get('sqft_basement')) 
    l.append(street()) 
    l.append(city()) 
    l.append(statezip()) 
    l.append(country()) 
    l.append(float(request.form.get('yr_built'))) 
    l.append(float(request.form.get('yr_renovated'))) 
    arr = np.array(l) 
    arr=arr.reshape(1,-1) 
prediction = round(model.predict(arr)[0],2) 
print(prediction) 
    return render_template('index.html') 
if _name=='main_': 
    app.run(port=5000,debug=True) 

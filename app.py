import joblib
model = joblib.load('./rf_model.joblib')        # Importing the model

import pickle
pickle_model = pickle.load(open('pickle_model.pkl','rb'))
from flask import Flask, render_template, request, jsonify



app = Flask(__name__)

@app.route(rule = '/')
def welcome():
    return render_template('GeeksFiesta.html')


@app.route('/predict', methods = ['POST'])
def predict():
    
    # year = float(request.form['Year'])
    # Month = float(request.form['Month'])
    # Day = float(request.form['Day'])
    # Hour = float(request.form['Hour'])
    Temperature = float(request.form['Temperature'])
    Pressure = float(request.form['Pressure'])
    Rain = float(request.form['Rain'])
    Wind_Speed = float(request.form['Wind_Speed'])

    feature_vector = [[Temperature, Pressure, Rain, Wind_Speed]]
    Pm_ = round(pickle_model.predict(feature_vector)[0], ndigits=2)
    output_ = f"The Predicted Value of PM2.5 at the given features is {Pm_}"

    return render_template('GeeksFiesta.html', Output_displayed = output_)


if __name__ == '__main__':
    app.run(debug = True)

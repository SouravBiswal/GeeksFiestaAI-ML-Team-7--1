import joblib
model = joblib.load('./rf_model.joblib')        # Importing the model

import re
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route(rule = '/')
def welcome():
    return render_template('GeeksFiesta.html')

# Result Checker HTML page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        year = float(request.form['Year'])
        Month = float(request.form['Month'])
        Day = float(request.form['Day'])
        Hour = float(request.form['Hour'])
        Temperature = float(request.form['Temperature'])
        Pressure = float(request.form['Pressure'])
        Rain = float(request.form['Rain'])
        Wind_Speed = float(request.form['Wind_Speed'])

        feature_vector = [[Temperature, Pressure, Rain, Wind_Speed]]
        Pm_ = round(model.predict(feature_vector)[0], ndigits=2)
        output_ = f"The Predicted Value of PM2.5 at the given features is {Pm_}"

    return render_template('GeeksFiesta.html', Output_displayed = output_)




if __name__ == '__main__':
    app.run(debug = True)       

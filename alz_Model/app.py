'''
from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for sessions

# Load the trained Random Forest model and encoder dictionary
rf_model = joblib.load('models/rf_model.pkl')
encoder_dict = joblib.load('models/encoder_dict.pkl')

@app.route('/')
def index():
    return render_template('demographic.html')

@app.route('/lifestyle', methods=['GET'])
def lifestyle():
    # Collect data from the 'demographic.html' page
    session['age'] = request.args.get('age')
    session['gender'] = request.args.get('gender')
    
    return render_template('lifestyle.html')

@app.route('/lifestyle_form', methods=['GET'])
def lifestyle_form():
    # Collect data from the 'lifestyle.html' page
    session['smoking'] = request.args.get('smoking')
    session['alcohol'] = request.args.get('alcohol')
    
    return redirect(url_for('medical_history'))

@app.route('/medical_history', methods=['GET'])
def medical_history():
    # Collect data from 'medical_history.html' page
    session['hypertension'] = request.args.get('hypertension')
    session['diabetes'] = request.args.get('diabetes')
    
    return render_template('medical_history.html')

@app.route('/clinical_measurements', methods=['GET'])
def clinical_measurements():
    # Collect data from 'clinical_measurements.html' page
    session['SystolicBP'] = request.args.get('SystolicBP')
    session['DiastolicBP'] = request.args.get('DiastolicBP')
    session['CholesterolTotal'] = request.args.get('CholesterolTotal')
    session['CholesterolLDL'] = request.args.get('CholesterolLDL')
    session['CholesterolHDL'] = request.args.get('CholesterolHDL')
    session['CholesterolTriglycerides'] = request.args.get('CholesterolTriglycerides')
    
    return redirect(url_for('cognitive_assessments'))

@app.route('/cognitive_assessments', methods=['GET'])
def cognitive_assessments():
    # Collect data from 'cognitive_assessments.html' page
    session['MMSE'] = request.args.get('MMSE')
    session['FunctionalAssessment'] = request.args.get('FunctionalAssessment')
    session['MemoryComplaints'] = request.args.get('MemoryComplaints')
    session['BehavioralProblems'] = request.args.get('BehavioralProblems')
    session['ADL'] = request.args.get('ADL')
    
    return redirect(url_for('symptoms'))

@app.route('/symptoms', methods=['GET'])
def symptoms():
    # Collect data from 'symptoms.html' page
    session['Confusion'] = request.args.get('Confusion')
    session['Disorientation'] = request.args.get('Disorientation')
    session['PersonalityChanges'] = request.args.get('PersonalityChanges')
    session['DifficultyCompletingTasks'] = request.args.get('DifficultyCompletingTasks')
    session['Forgetfulness'] = request.args.get('Forgetfulness')

    # Convert input data into the proper format for the model
    model_input = np.array([[
        session['SystolicBP'], session['DiastolicBP'],
        session['CholesterolTotal'], session['CholesterolLDL'],
        session['CholesterolHDL'], session['CholesterolTriglycerides'],
        session['MMSE'], session['FunctionalAssessment'],
        session['MemoryComplaints'], session['BehavioralProblems'],
        session['ADL'], session['Confusion'],
        session['Disorientation'], session['PersonalityChanges'],
        session['DifficultyCompletingTasks'], session['Forgetfulness']
    ]])

    # Make the prediction
    prediction = rf_model.predict(model_input)

    # Return the prediction result to the results page
    return render_template('results.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np

app = Flask(__name__)

# Dynamically generate a secret key (useful for development)
app.secret_key = os.urandom(24)  # This generates a random 24-byte secret key

# Load the trained Random Forest model and encoder dictionary
rf_model = joblib.load('models/rf_model.pkl')
encoder_dict = joblib.load('models/encoder_dict.pkl')

@app.route('/')
def index():
    return render_template('demographic.html')

@app.route('/templates/lifestyle', methods=['GET'])
def lifestyle():
    if request.method == 'GET':
        # Collect data from the 'demographic.html' page using query parameters
        session['age'] = request.args.get('age')
        session['gender'] = request.args.get('gender')
        session['ethnicity'] = request.args.get('ethnicity')
        return render_template('lifestyle.html')

@app.route('/lifestyle_form', methods=['GET'])
def lifestyle_form():
    # Collect data from the 'lifestyle.html' page using query parameters
    session['bmi'] = request.args.get('bmi')
    session['smoking'] = request.args.get('smoking')
    session['alcohol'] = request.args.get('alcohol')
    session['physicalActivity'] = request.args.get('physicalActivity')
    session['dietQuality'] = request.args.get('dietQuality')
    session['sleepQuality'] = request.args.get('sleepQuality')

    return redirect(url_for('medical_history'))

@app.route('/medical_history', methods=['GET'])
def medical_history():
    # Collect data from 'medical_history.html' page using query parameters
    session['familyHistory'] = request.args.get('familyHistory')
    session['cardiovascularDisease'] = request.args.get('cardiovascularDisease')
    session['hypertension'] = request.args.get('hypertension')
    session['diabetes'] = request.args.get('diabetes')
    
    return redirect(url_for('clinical_measurements'))

@app.route('/clinical_measurements', methods=['GET'])
def clinical_measurements():
    # Collect data from 'clinical_measurements.html' page using query parameters
    session['SystolicBP'] = request.args.get('systolicBP')
    session['DiastolicBP'] = request.args.get('diastolicBP')
    session['CholesterolTotal'] = request.args.get('cholesterolTotal')
    session['CholesterolLDL'] = request.args.get('cholesterolLDL')
    session['CholesterolHDL'] = request.args.get('cholesterolHDL')
    session['CholesterolTriglycerides'] = request.args.get('cholesterolTriglycerides')

    return redirect(url_for('cognitive_assessments'))

@app.route('/cognitive_assessments', methods=['GET'])
def cognitive_assessments():
    # Collect data from 'cognitive_assessments.html' page using query parameters
    session['MMSE'] = request.args.get('mmse')
    session['FunctionalAssessment'] = request.args.get('functionalAssessment')
    session['MemoryComplaints'] = request.args.get('memoryComplaints')
    session['BehavioralProblems'] = request.args.get('behavioralProblems')
    session['ADL'] = request.args.get('adl')

    return redirect(url_for('symptoms'))


import os
from flask import Flask, render_template, request, jsonify, session
import joblib
import numpy as np

app = Flask(__name__)

# Dynamically generate a secret key (useful for development)
app.secret_key = os.urandom(24)  # This generates a random 24-byte secret key

# Load the trained Random Forest model and encoder dictionary
rf_model = joblib.load('models/rf_model.pkl')
encoder_dict = joblib.load('models/encoder_dict.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect data from the request form
    data = request.json

    # Store in session (optional)
    session['data'] = data

    # Prepare input data for model prediction
    model_input = np.array([[
        data['SystolicBP'], data['DiastolicBP'],
        data['CholesterolTotal'], data['CholesterolLDL'],
        data['CholesterolHDL'], data['CholesterolTriglycerides'],
        data['MMSE'], data['FunctionalAssessment'],
        data['MemoryComplaints'], data['BehavioralProblems'],
        data['ADL'], data['Confusion'],
        data['Disorientation'], data['PersonalityChanges'],
        data['DifficultyCompletingTasks'], data['Forgetfulness']
    ]])

    # Make the prediction
    prediction = rf_model.predict(model_input)

    # Return the prediction result as JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained Random Forest model and encoder dictionary
rf_model = joblib.load('models/rf_model.pkl')
encoder_dict = joblib.load('models/encoder_dict.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    input_data = {
        'Age': float(request.form['age']),
        'Gender': int(request.form['gender']),
        'Ethnicity': int(request.form['ethnicity']),
        'EducationLevel': int(request.form['education_level']),
        'BMI': float(request.form['bmi']),
        'Smoking': int(request.form['smoking']),
        'AlcoholConsumption': float(request.form['alcohol_consumption']),
        'PhysicalActivity': float(request.form['physical_activity']),
        'DietQuality': float(request.form['diet_quality']),
        'SleepQuality': float(request.form['sleep_quality']),
        'FamilyHistoryAlzheimers': int(request.form['family_history']),
        'CardiovascularDisease': int(request.form['cardiovascular_disease']),
        'Diabetes': int(request.form['diabetes']),
        'Depression': int(request.form['depression']),
        'HeadInjury': int(request.form['head_injury']),
        'Hypertension': int(request.form['hypertension']),
        'SystolicBP': float(request.form['systolic_bp']),
        'DiastolicBP': float(request.form['diastolic_bp']),
        'CholesterolTotal': float(request.form['cholesterol_total']),
        'CholesterolLDL': float(request.form['cholesterol_ldl']),
        'CholesterolHDL': float(request.form['cholesterol_hdl']),
        'CholesterolTriglycerides': float(request.form['cholesterol_triglycerides']),
        'MMSE': float(request.form['mmse']),
        'FunctionalAssessment': float(request.form['functional_assessment']),
        'MemoryComplaints': int(request.form['memory_complaints']),
        'BehavioralProblems': int(request.form['behavioral_problems']),
        'ADL': float(request.form['adl']),
        'Confusion': int(request.form['confusion']),
        'Disorientation': int(request.form['disorientation']),
        'PersonalityChanges': int(request.form['personality_changes']),
        'DifficultyCompletingTasks': int(request.form['difficulty_completing_tasks']),
        'Forgetfulness': int(request.form['forgetfulness']),
    }

    # Convert input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Preprocess the data (apply encoding based on encoder_dict)
    for column in encoder_dict:
        if column in input_df.columns:
            encoder = encoder_dict[column]
            input_df[column] = encoder.transform(input_df[column])

    # Make predictions using the trained model
    predictions = rf_model.predict(input_df)

    # Return the result on a new webpage
    return render_template('results.html', prediction=predictions[0])

if __name__ == '__main__':
    app.run(debug=True,port=5500)

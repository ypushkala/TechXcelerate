import streamlit as st
import joblib
import pandas as pd

# Load the trained Random Forest model and encoder dictionary
rf_model = joblib.load('alz_Model/models/rf_model.pkl')
encoder_dict = joblib.load('alz_Model/models/encoder_dict.pkl')

def main():
    st.title("Alzheimer's Disease Risk Prediction")
    
    # Collect input data from the user
    age = st.number_input('Age', min_value=0)
    gender = st.selectbox('Gender', [0, 1])
    ethnicity = st.selectbox('Ethnicity', [0, 1, 2, 3, 4])
    education_level = st.selectbox('Education Level', [0, 1, 2, 3, 4])
    bmi = st.number_input('BMI', min_value=0.0)
    smoking = st.selectbox('Smoking', [0, 1])
    alcohol_consumption = st.number_input('Alcohol Consumption', min_value=0.0)
    physical_activity = st.number_input('Physical Activity', min_value=0.0)
    diet_quality = st.number_input('Diet Quality', min_value=0.0)
    sleep_quality = st.number_input('Sleep Quality', min_value=0.0)
    family_history = st.selectbox('Family History of Alzheimer’s', [0, 1])
    cardiovascular_disease = st.selectbox('Cardiovascular Disease', [0, 1])
    diabetes = st.selectbox('Diabetes', [0, 1])
    depression = st.selectbox('Depression', [0, 1])
    head_injury = st.selectbox('Head Injury', [0, 1])
    hypertension = st.selectbox('Hypertension', [0, 1])
    systolic_bp = st.number_input('Systolic BP', min_value=0.0)
    diastolic_bp = st.number_input('Diastolic BP', min_value=0.0)
    cholesterol_total = st.number_input('Total Cholesterol', min_value=0.0)
    cholesterol_ldl = st.number_input('LDL Cholesterol', min_value=0.0)
    cholesterol_hdl = st.number_input('HDL Cholesterol', min_value=0.0)
    cholesterol_triglycerides = st.number_input('Triglycerides', min_value=0.0)
    mmse = st.number_input('MMSE', min_value=0.0)
    functional_assessment = st.number_input('Functional Assessment', min_value=0.0)
    memory_complaints = st.selectbox('Memory Complaints', [0, 1])
    behavioral_problems = st.selectbox('Behavioral Problems', [0, 1])
    adl = st.number_input('ADL', min_value=0.0)
    confusion = st.selectbox('Confusion', [0, 1])
    disorientation = st.selectbox('Disorientation', [0, 1])
    personality_changes = st.selectbox('Personality Changes', [0, 1])
    difficulty_completing_tasks = st.selectbox('Difficulty Completing Tasks', [0, 1])
    forgetfulness = st.selectbox('Forgetfulness', [0, 1])

    # When the user clicks the 'Predict' button
    if st.button('Predict'):
        # Create input dataframe
        input_data = {
            'Age': age,
            'Gender': gender,
            'Ethnicity': ethnicity,
            'EducationLevel': education_level,
            'BMI': bmi,
            'Smoking': smoking,
            'AlcoholConsumption': alcohol_consumption,
            'PhysicalActivity': physical_activity,
            'DietQuality': diet_quality,
            'SleepQuality': sleep_quality,
            'FamilyHistoryAlzheimers': family_history,
            'CardiovascularDisease': cardiovascular_disease,
            'Diabetes': diabetes,
            'Depression': depression,
            'HeadInjury': head_injury,
            'Hypertension': hypertension,
            'SystolicBP': systolic_bp,
            'DiastolicBP': diastolic_bp,
            'CholesterolTotal': cholesterol_total,
            'CholesterolLDL': cholesterol_ldl,
            'CholesterolHDL': cholesterol_hdl,
            'CholesterolTriglycerides': cholesterol_triglycerides,
            'MMSE': mmse,
            'FunctionalAssessment': functional_assessment,
            'MemoryComplaints': memory_complaints,
            'BehavioralProblems': behavioral_problems,
            'ADL': adl,
            'Confusion': confusion,
            'Disorientation': disorientation,
            'PersonalityChanges': personality_changes,
            'DifficultyCompletingTasks': difficulty_completing_tasks,
            'Forgetfulness': forgetfulness,
        }

        input_df = pd.DataFrame([input_data])

        # Preprocess the data (apply encoding based on encoder_dict)
        for column in encoder_dict:
            if column in input_df.columns:
                encoder = encoder_dict[column]
                input_df[column] = encoder.transform(input_df[column])

        # Make predictions using the trained model
        predictions = rf_model.predict(input_df)

        # Display the result
        st.success(f'The predicted risk score is: {predictions[0]}')

if __name__ == '__main__':
    main()

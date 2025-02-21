import joblib
import pandas as pd

# Load the trained Random Forest model and encoder dictionary
rf_model = joblib.load('models/rf_model.pkl')
encoder_dict = joblib.load('models/encoder_dict.pkl')

# Example input data (mock values)
input_data = [
    {'Age': 70, 'Gender': 1, 'Ethnicity': 1, 'EducationLevel': 2, 'BMI': 25.0, 
     'Smoking': 0, 'AlcoholConsumption': 10.0, 'PhysicalActivity': 5.0, 
     'DietQuality': 7.0, 'SleepQuality': 8.0, 'FamilyHistoryAlzheimers': 1, 
     'CardiovascularDisease': 0, 'Diabetes': 0, 'Depression': 0, 'HeadInjury': 0, 
     'Hypertension': 0, 'SystolicBP': 120, 'DiastolicBP': 80, 'CholesterolTotal': 200, 
     'CholesterolLDL': 100, 'CholesterolHDL': 50, 'CholesterolTriglycerides': 150, 
     'MMSE': 27, 'FunctionalAssessment': 6, 'MemoryComplaints': 0, 'BehavioralProblems': 0, 
     'ADL': 7, 'Confusion': 0, 'Disorientation': 0, 'PersonalityChanges': 0, 
     'DifficultyCompletingTasks': 0, 'Forgetfulness': 0}
    # Add more records if needed
]

# Convert input data into a DataFrame
input_df = pd.DataFrame(input_data)

# Preprocess the data (apply encoding based on encoder_dict)
for column in encoder_dict:
    if column in input_df.columns:
        # Get the encoder for the column
        encoder = encoder_dict[column]
        
        # Transform the categorical column using the encoder's 'transform' method
        input_df[column] = encoder.transform(input_df[column])

# Ensure the input data has the same columns and format the model expects
# If you need to perform additional preprocessing (like scaling), apply it here

# Make predictions using the trained model
predictions = rf_model.predict(input_df)

# Print the predictions
print("Predictions:", predictions)

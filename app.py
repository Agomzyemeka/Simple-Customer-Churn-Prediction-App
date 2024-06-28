%%writefile app.py

import streamlit as st
import pandas as pd
import joblib

# Load the saved model and scaler
best_model = joblib.load('best_model_Random Forest.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit UI
st.title('Customer Churn Prediction')

st.header('Enter customer details:')

# User inputs
CreditScore = st.number_input('Credit Score', min_value=300, max_value=900, value=600)
Geography = st.selectbox('Geography', ('France', 'Spain', 'Germany'))
Gender = st.selectbox('Gender', ('Male', 'Female'))
Age = st.number_input('Age', min_value=18, max_value=100, value=40)
Tenure = st.number_input('Tenure (years)', min_value=0, max_value=10, value=5)
Balance = st.number_input('Balance', min_value=0, value=60000)
NumOfProducts = st.number_input('Number of Products', min_value=1, max_value=4, value=2)
HasCrCard = st.selectbox('Has Credit Card?', ('Yes', 'No'))
IsActiveMember = st.selectbox('Is Active Member?', ('Yes', 'No'))
EstimatedSalary = st.number_input('Estimated Salary', min_value=0, value=50000)

# Convert categorical inputs to numerical
Geography_dict = {'France': 0, 'Spain': 1, 'Germany': 2}
Gender_dict = {'Male': 0, 'Female': 1}
HasCrCard_dict = {'No': 0, 'Yes': 1}
IsActiveMember_dict = {'No': 0, 'Yes': 1}

# Create a dataframe for the input
input_data = pd.DataFrame({
    'CreditScore': [CreditScore],
    'Geography': [Geography_dict[Geography]],
    'Gender': [Gender_dict[Gender]],
    'Age': [Age],
    'Tenure': [Tenure],
    'Balance': [Balance],
    'NumOfProducts': [NumOfProducts],
    'HasCrCard': [HasCrCard_dict[HasCrCard]],
    'IsActiveMember': [IsActiveMember_dict[IsActiveMember]],
    'EstimatedSalary': [EstimatedSalary]
})

# Standardize the input data
input_data_scaled = scaler.transform(input_data)

# Predict churn
if st.button('Predict'):
    prediction = best_model.predict(input_data_scaled)
    result = 'Yes' if prediction[0] == 1 else 'No'
    st.write(f'Will the customer churn? {result}')

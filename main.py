# codebasics ML course: codebasics.io, all rights reserved
import streamlit as st
from prediction_helper import predict

# Page configuration
st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="🏥", layout="wide")

# Custom CSS for a modern look
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
        padding: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 5px;
        border: none;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: white;
        border-radius: 5px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #2c3e50;
        color: white;
        text-align: center;
        padding: 10px 0;
    }
    .instruction-box {
        background-color: #e8f4f8;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and developer info
st.markdown("<h1 style='text-align: center;'>Health Insurance Cost Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Developed by Erick Kiprotich Yegon, PhD</h3>", unsafe_allow_html=True)

# Instructions
st.markdown("""
    <div class="instruction-box">
    <h3>Instructions:</h3>
    <ol>
        <li>Fill in all the fields with your personal and health information.</li>
        <li>Select appropriate options from the dropdown menus.</li>
        <li>For income, enter the amount in ten thousands of Shillings (e.g., 50 = 500,000 Shillings).</li>
        <li>Click the 'Predict' button to get your estimated health insurance cost.</li>
        <li>The prediction will appear below the button.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# Define the categorical options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Nairobi', 'Central', 'Coast', 'Eastern', 'North Eastern', 'Nyanza', 'Rift Valley', 'Western'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_ten_thousands = st.number_input('Income (in ten thousands of Shillings)', step=1, min_value=0, max_value=10000)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Ten Thousands': income_ten_thousands,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>Predicted Health Insurance Cost: {prediction}</h2>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2024 Health Insurance Cost Predictor | codebasics ML course: codebasics.io, all rights reserved</p>
    </div>
    """, unsafe_allow_html=True)
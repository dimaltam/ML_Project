import streamlit as st
import pandas as pd
import pickle

# Load pipeline model
model = pickle.load(open("final_model.pkl", "rb"))

# Title
st.title("🚴‍♂️ Bike Buyer Prediction App")

# UI inputs
st.header("Enter User Details")

with st.form("input_form"):
    user_id = st.text_input("User ID", value="12345")  # placeholder ID

    col1, col2 = st.columns(2)
    with col1:
        marital_status = st.selectbox("Marital Status", ['Single', 'Married'])
        gender = st.selectbox("Gender", ['Male', 'Female'])
        home_owner = st.selectbox("Home Owner", ['Yes', 'No'])
        region = st.selectbox("Region", ['North', 'South', 'East', 'West'])

    with col2:
        occupation = st.selectbox("Occupation", ['Professional', 'Skilled Manual', 'Clerical', 'Management', 'Manual', 'Others'])
        commute = st.selectbox("Commute Distance", ['0-1 Miles', '1-2 Miles', '2-5 Miles', '5-10 Miles', '10+ Miles'])
        education = st.selectbox("Education", ['Partial High School', 'High School', 'Partial College', 'Bachelors', 'Graduate Degree'])

    age = st.slider("Age", 18, 100, 30)
    income = st.number_input("Yearly Income", min_value=0, value=50000)
    children = st.slider("Number of Children", 0, 10, 0)
    cars = st.slider("Number of Cars Owned", 0, 5, 0)

    submit = st.form_submit_button("Predict")

if submit:
    # Add 'ID' field to match training columns
    input_data = pd.DataFrame([{
        'ID': user_id,
        'Marital Status': marital_status,
        'Gender': gender,
        'Home Owner': home_owner,
        'Region': region,
        'Occupation': occupation,
        'Commute Distance': commute,
        'Education': education,
        'Age': age,
        'Income': income,
        'Children': children,
        'Cars': cars
    }])

    try:
        prediction = model.predict(input_data)[0]
        label = "✅ Will Buy a Bike" if prediction == 1 else "❌ Will Not Buy a Bike"
        st.success(f"Prediction: {label}")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

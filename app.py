import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("linear_model.pkl")

# Define label encoding mappings (must match your training phase)
sex_map = {"Male": 0.0, "Female": 1.0}
smoker_map = {"No": 0.0, "Yes": 1.0}
day_map = {"Thur": 0.0, "Fri": 1.0, "Sat": 2.0, "Sun": 3.0}
time_map = {"Lunch": 0.0, "Dinner": 1.0}

# Page setup
st.set_page_config(page_title="Tip Predictor", layout="centered")
st.title("💡 Tip Prediction App")
st.write("Predict the tip based on customer details and bill info.")


total_bill = st.slider("Total Bill ($)", 3.07, 44.30, step=0.1)
sex_input = st.selectbox("Gender", options=list(sex_map.keys()))
smoker_input = st.selectbox("Smoker", options=list(smoker_map.keys()))
day_input = st.selectbox("Day", options=list(day_map.keys()))
time_input = st.selectbox("Time", options=list(time_map.keys()))
size = st.slider("Group Size", 1, 6, step=1)

# Encode categorical inputs
sex = sex_map[sex_input]
smoker = smoker_map[smoker_input]
day = day_map[day_input]
time = time_map[time_input]

# Derived features
bill_per_person = total_bill / size
tip_per_person = st.slider("Tip Per Person (estimation)", 0.4, 2.925, step=0.01, value=1.5)
big_party = 1.0 if size >= 5 else 0.0

# Prepare input vector
input_features = np.array([[total_bill, sex, smoker, day, time, size, bill_per_person, tip_per_person, big_party]])

# Predict
if st.button("Predict Tip"):
    prediction = model.predict(input_features)[0]
    st.success(f"💰 Predicted Tip: **${prediction:.2f}**")

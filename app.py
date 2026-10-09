import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("students.csv")

# Features and target
X = data[["study_hours", "attendance", "previous_marks"]]
y = data["performance"]

# Create and train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Page title
st.title("🎓 Student Performance Predictor")

st.write("Enter the student's details to predict performance.")

# User inputs
study_hours = st.number_input(
    "Study hours per day",
    min_value=0,
    max_value=24,
    value=2,
    step=1
)

attendance = st.number_input(
    "Attendance percentage",
    min_value=0,
    max_value=100,
    value=75,
    step=1
)

previous_marks = st.number_input(
    "Previous marks",
    min_value=0,
    max_value=100,
    value=60,
    step=1
)

# Prediction button
if st.button("Predict Performance"):

    new_student = pd.DataFrame(
        [[study_hours, attendance, previous_marks]],
        columns=["study_hours", "attendance", "previous_marks"]
    )

    prediction = model.predict(new_student)

    if prediction[0] == 1:
        st.success("Good Performance")
    else:
        st.warning("Needs Improvement")
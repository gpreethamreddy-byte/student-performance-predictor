import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("students.csv")

# Features and target
X = data[["study_hours", "attendance", "previous_marks"]]
y = data["performance"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Get student information
print("\n--- Student Performance Predictor ---")

try:
    study_hours = float(input("Enter study hours per day: "))
    attendance = float(input("Enter attendance percentage: "))
    previous_marks = float(input("Enter previous marks: "))

    if study_hours < 0 or study_hours > 24:
        print("Study hours must be between 0 and 24.")
        exit()

    if attendance < 0 or attendance > 100:
        print("Attendance must be between 0 and 100.")
        exit()

    if previous_marks < 0 or previous_marks > 100:
        print("Previous marks must be between 0 and 100.")
        exit()

except ValueError:
    print("Please enter numbers only.")
    exit()
# Create DataFrame
new_student = pd.DataFrame(
    [[study_hours, attendance, previous_marks]],
    columns=["study_hours", "attendance", "previous_marks"]
)

# Make prediction
prediction = model.predict(new_student)

# Display result
if prediction[0] == 1:
    print("\nPrediction: Good Performance")
    print("The student is likely to perform well.")
else:
    print("\nPrediction: Needs Improvement")
    print("The student may need to improve study habits.")
# import pandas as pd

# data = pd.read_csv("students.csv")

# print("First 5 students:")
# print(data.head())

# print("\nDataset information:")
# print(data.info())
# import pandas as pd

# data = pd.read_csv("students.csv")

# X = data[["study_hours", "attendance", "previous_marks"]]
# y = data["performance"]

# print("Input data:")
# print(X)

# print("\nOutput data:")
# print(y)
# import pandas as pd

# from sklearn.model_selection import train_test_split

# data = pd.read_csv("students.csv")

# X = data[["study_hours", "attendance", "previous_marks"]]
# y = data["performance"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# print("Training data:")
# print(X_train)

# print("\nTesting data:")
# print(X_test)
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load data
data = pd.read_csv("students.csv")

# Input and output
X = data[["study_hours", "attendance", "previous_marks"]]
y = data["performance"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

print("Model training completed!")
# Test the model
predictions = model.predict(X_test)

print("\nActual values:")
print(y_test.values)

print("\nPredicted values:")
print(predictions)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")
# Predict for a new student

print("\n--- New Student Prediction ---")

study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_marks = float(input("Enter previous marks: "))

new_student = pd.DataFrame(
    [[study_hours, attendance, previous_marks]],
    columns=["study_hours", "attendance", "previous_marks"]
)

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: Good Performance")
else:
    print("Prediction: Needs Improvement")

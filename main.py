print("Student Performance Predictor")

name = input("Enter your name: ")
study_hours = float(input("Enter your daily study hours: "))
attendance = float(input("Enter your attendance percentage: "))

print("\nStudent Details")
print("Name:", name)
print("Study Hours:", study_hours)
print("Attendance:", attendance, "%")

# Prediction
if study_hours >= 3 and attendance >= 75:
    result = "Good Performance"
else:
    result = "Needs Improvement"

print("\nPrediction:", result)
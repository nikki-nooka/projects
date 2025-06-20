import webbrowser
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# ==============================
# Data Preparation and Model
# ==============================

# Sample dataset
data = [
    [5, 90, 75, 'B'],
    [3, 65, 50, 'D'],
    [8, 95, 85, 'A'],
    [2, 50, 40, 'F'],
    [6, 75, 65, 'C'],
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['StudyHours', 'Attendance', 'PreviousScore', 'Grade'])

# Encode Grades
le = LabelEncoder()
df['GradeEncoded'] = le.fit_transform(df['Grade'])

# Feature and target
X = df[['StudyHours', 'Attendance', 'PreviousScore']]
y = df['GradeEncoded']

# Train model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# ==============================
# Prediction Function
# ==============================

def predict_grade_rf(study_hours, attendance, prev_score):
    prediction = rf_model.predict([[study_hours, attendance, prev_score]])[0]
    grade = le.inverse_transform([prediction])[0]
    weighted_score = rf_model.predict_proba([[study_hours, attendance, prev_score]])[0].max() * 10
    return grade, weighted_score

# ==============================
# Visualization Functions
# ==============================

def create_bar_chart(study, attend, prev, weighted_score):
    categories = ['Study Hours', 'Attendance', 'Previous Score', 'Confidence Score']
    values = [study, attend / 10, prev / 10, weighted_score]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, values, color=['#3498db', '#2ecc71', '#f1c40f', '#e74c3c'])

    ax.set_ylabel('Score')
    ax.set_title('Student Performance Metrics')
    ax.set_ylim(0, 10)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}', ha='center', va='bottom')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def create_pie_chart(grade_distribution):
    labels = ['A', 'B', 'C', 'D', 'F']
    sizes = [grade_distribution.get(g, 0) for g in labels]
    colors = ['#2ecc71', '#3498db', '#f1c40f', '#e67e22', '#e74c3c']

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Class Grade Distribution')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# ==============================
# HTML Report Generation
# ==============================

def create_html_page(grade, weighted_score, study, attend, prev):
    grade_dist = df['Grade'].value_counts().to_dict()
    bar_chart = create_bar_chart(study, attend, prev, weighted_score)
    pie_chart = create_pie_chart(grade_dist)

    html_content = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Grade Prediction</title>
        <style>
            body {{ font-family: Arial; margin: 40px; background-color: #f9f9f9; }}
            .result {{ background: white; padding: 20px; border-radius: 10px; max-width: 800px; margin: auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
            .grade {{ font-size: 72px; color: #2ecc71; }}
            table {{ width: 100%; margin-top: 20px; border-collapse: collapse; }}
            th, td {{ padding: 12px; border: 1px solid #ddd; }}
            th {{ background-color: #f2f2f2; }}
            .chart-container {{ display: flex; gap: 20px; margin-top: 30px; }}
            .chart {{ flex: 1; border: 1px solid #eee; padding: 10px; border-radius: 5px; background: white; }}
            .btn {{ padding: 10px 20px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px; margin-top: 20px; display: inline-block; }}
            .btn:hover {{ background-color: #2980b9; }}
        </style>
    </head>
    <body>
        <div class="result">
            <h1>Grade Prediction Result</h1>
            <div class="grade">{grade}</div>
            <p>Model Confidence Score: {weighted_score:.2f}</p>
            <table>
                <tr><th>Criteria</th><th>Value</th></tr>
                <tr><td>Study Hours</td><td>{study} hours/day</td></tr>
                <tr><td>Attendance</td><td>{attend}%</td></tr>
                <tr><td>Previous Score</td><td>{prev}</td></tr>
            </table>
            <div class="chart-container">
                <div class="chart"><img src="data:image/png;base64,{bar_chart}" style="width:100%;"></div>
                <div class="chart"><img src="data:image/png;base64,{pie_chart}" style="width:100%;"></div>
            </div>
            <a href="#" class="btn" onclick="window.history.back()">Predict Another</a>
        </div>
    </body>
    </html>"""

    with open("grades_rf.html", "w") as f:
        f.write(html_content)

    return Path("grades_rf.html").absolute()

# ==============================
# Command-Line Interface
# ==============================

if __name__ == "__main__":
    print("STUDENT GRADE PREDICTOR USING RANDOM FOREST")
    print("-------------------------------------------")

    while True:
        try:
            print("\nEnter student details (or 'q' to quit):")
            study = input("Study hours/day (1-10): ")
            if study.lower() == 'q':
                break
            study = float(study)
            attend = float(input("Attendance % (0-100): "))
            prev = float(input("Previous test score (0-100): "))

            grade, weighted_score = predict_grade_rf(study, attend, prev)
            html_file = create_html_page(grade, weighted_score, study, attend, prev)

            print(f"\nPREDICTED GRADE: {grade} (Confidence Score: {weighted_score:.2f})")
            print("Opening results in browser...")
            webbrowser.open(f"file://{html_file}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")
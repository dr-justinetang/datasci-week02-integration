#!/usr/bin/env python3
# src/data_analysis.py
import os

def load_students(filename):
    """Read CSV and return list of student data"""
    students = []
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]  # skip header
        for line in lines:
            name, age, grade, subject = line.strip().split(',')
            students.append({
                'name': name,
                'age': int(age),
                'grade': int(grade),
                'subject': subject
            })
    return students

def calculate_average_grade(students):
    grades = [s['grade'] for s in students]
    return sum(grades) / len(grades)

def count_math_students(students):
    return sum(1 for s in students if s['subject'] == 'Math')

def generate_report(students):
    total = len(students)
    avg_grade = calculate_average_grade(students)
    math_count = count_math_students(students)

    report = f"Total number of students: {total}\n"
    report += f"Average grade: {avg_grade:.1f}\n"
    report += f"Number of Math students: {math_count}\n"
    return report

def save_report(report, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(report)

def main():
    students = load_students('data/students.csv')
    report = generate_report(students)
    save_report(report, 'output/analysis_report.txt')
    print("Basic analysis complete. Report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# src/data_analysis_functions.py
import os

def load_csv(filename):
    """Load CSV data"""
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

def analyze_grade_distribution(grades):
    """Count grades by letter ranges"""
    dist = {'A':0,'B':0,'C':0,'D':0,'F':0}
    for g in grades:
        if g >= 90:
            dist['A'] += 1
        elif g >= 80:
            dist['B'] += 1
        elif g >= 70:
            dist['C'] += 1
        elif g >= 60:
            dist['D'] += 1
        else:
            dist['F'] += 1
    return dist

def analyze_data(students):
    """Return dictionary with statistics"""
    total = len(students)
    grades = [s['grade'] for s in students]

    subjects = {}
    for s in students:
        subjects[s['subject']] = subjects.get(s['subject'], 0) + 1

    grade_dist = analyze_grade_distribution(grades)

    return {
        'total': total,
        'average': sum(grades)/total,
        'highest': max(grades),
        'lowest': min(grades),
        'subjects': subjects,
        'grade_distribution': grade_dist
    }

def save_results(results, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(f"Total number of students: {results['total']}\n")
        f.write(f"Average grade: {results['average']:.1f}\n")
        f.write(f"Highest grade: {results['highest']}\n")
        f.write(f"Lowest grade: {results['lowest']}\n\n")
        f.write("Students per subject:\n")
        for sub, count in results['subjects'].items():
            f.write(f"  {sub}: {count}\n")
        f.write("\nGrade distribution:\n")
        for grade, count in results['grade_distribution'].items():
            percent = (count/results['total'])*100
            f.write(f"  {grade}: {count} ({percent:.1f}%)\n")

def main():
    students = load_csv('data/students.csv')
    results = analyze_data(students)
    save_results(results, 'output/analysis_report.txt')
    print("Advanced analysis complete. Report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()

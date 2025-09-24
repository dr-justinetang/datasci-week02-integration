#!/usr/bin/env python3
# src/data_analysis_functions.py
import os

def load_data(filename):
    """Generic loader that checks file extension"""
    if filename.endswith('.csv'):
        return load_csv(filename)
    else:
        raise ValueError("Unsupported file type")

def load_csv(filename):
    """Load CSV file and return list of student dictionaries"""
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
    """Count letter grades (A-F)"""
    dist = {'A':0,'B':0,'C':0,'D':0,'F':0}
    for g in grades:
        if 90 <= g <= 100:
            dist['A'] += 1
        elif 80 <= g <= 89:
            dist['B'] += 1
        elif 70 <= g <= 79:
            dist['C'] += 1
        elif 60 <= g <= 69:
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
    students = load_data('data/students.csv')
    results = analyze_data(students)
    save_results(results, 'output/analysis_report.txt')
    print("Advanced analysis complete. Report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()

import csv

students = []

with open("grades.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Grade"] = int(row["Grade"])
        students.append(row)

subject_grades = {}

for student in students:
    subject = student["Subject"]
    grade = student["Grade"]

    if subject not in subject_grades:
        subject_grades[subject] = []

    subject_grades[subject].append(grade)

with open("average_grades.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Subject", "Average Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for subject, grades in subject_grades.items():
        average = sum(grades) / len(grades)

        writer.writerow({
            "Subject": subject,
            "Average Grade": f"{average:g}"
        })

print("Average grades have been saved!")
import csv

# 1. Read data from grades.csv
students = []

with open("grades.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Grade"] = int(row["Grade"])
        students.append(row)

# 2. Calculate average grade
subject_grades = {}

for student in students:
    subject = student["Subject"]
    grade = student["Grade"]

    if subject not in subject_grades:
        subject_grades[subject] = []

    subject_grades[subject].append(grade)

# 3. Write results to average_grades.csv
with open("average_grades.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Subject", "Average Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for subject, grades in subject_grades.items():
        average = sum(grades) / len(grades)

        writer.writerow({
            "Subject": subject,
            "Average Grade": f"{average:g}"
        })

print("Average grades have been saved!")
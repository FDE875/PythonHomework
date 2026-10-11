universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(universities):
    students = []
    tuition_fees = []

    for university in universities:
        students.append(university[1])
        tuition_fees.append(university[2])

    return students, tuition_fees


def mean(values):
    return sum(values) / len(values)


def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    middle = n // 2

    if n % 2 == 1:
        return sorted_values[middle]
    else:
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2


students, tuition_fees = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition_fees)

student_mean = mean(students)
student_median = median(students)

tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)


print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("*" * 30)

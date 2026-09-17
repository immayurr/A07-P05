student_id = 101
student_name = "Arun Kumar"
course = "Computer Science"
semester = 5

marks = {
    "Python": 85,
    "Database": 78,
    "Operating Systems": 92,
    "Computer Networks": 88,
    "Software Engineering": 81
}
attendance = 92
total_marks = sum(marks.values())
average_marks = total_marks / len(marks)
print("Student Management and Academic Performance System")
print("-----------------------------------------------")
print("Student ID:", student_id)
print("Student Name:", student_name)
print("Course:", course)
print("Semester:", semester)
print("Attendance:", attendance, "%")
print("\nAcademic Performance:")
for subject, mark in marks.items():
    print(subject + ":", mark)
print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

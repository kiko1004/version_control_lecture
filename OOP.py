import random
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grades: list

names = ["Joro", "Mario", "Petko", "Ivo", "Ivana"]

students = [
    Student(name, [random.randint(2,6) for i in range(4)]) for name in names
]

def avg(itr) -> float:
    return sum(itr)/len(itr)

def find_grades_by_name(name: str, students: list) -> list:
    for student in students:
        if student.name == name:
            return student.grades
    else:
        raise NameError("Student not found!")

def find_the_excelent_student(students: list) -> str:
    winners = []
    avg_score = max([avg(student.grades) for student in students])

    for student in students:
        if avg(student.grades) == avg_score:
            winners.append(student)

    if len(winners) > 1:
        print(f"We have {len(winners)} winners!")
    for winner in winners:
        print(f"{winner.name} has the highest average of {avg_score}")

    return ", ".join([i.name for i in winners])


print(students)
student_name = find_the_excelent_student(students)
grades = find_grades_by_name(student_name, students)
print(grades)
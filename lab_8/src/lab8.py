from Students import (
    Student,
    StudentCollectionCM,
    StudentCollection,
)

print("Task A - Iteration")
print()

students = [
    Student("Gleb Senior", "КН-124", 96),
    Student("Gleb Junior", "КН-124", 94),
]

collection = StudentCollection(students)

for student in collection:
    print(student)

print()
print("What do we see: we can iterate over our custom collection using for loop")
print("Why does it work: because we implemented __iter__ and __next__ (iterator protocol)")

print("-------------------------------------------------")


print("Task B - Context Manager")
print()

with StudentCollectionCM(students) as collection:
    for student in collection:
        print(student)
    s = 1 / 0

print()
print("What do we see: messages before and after the block execution")
print("Why does it work: because __enter__ and __exit__  methods control the with statement")
print("'With' terminates even if a 'ZeroDivisionError' occurs, since the __exit__ handler returns True, which suppresses the error")

print("-------------------------------------------------")


print("Task C - Descriptor")
print()

student_test = Student("Kiril", "КН-125", 60)

print("Try to set an invalid grade (134):")

try:
    student_test.grade = 134
except ValueError as e:
    print("Error:", e)

print()
print("What do we see: invalid grade raises an error")
print("Why does it work: descriptor controls attribute assignment via __set__")

print("-------------------------------------------------")


print("Task D - Integration")
print()

students_full = [
    Student("Gleb Senior", "КН-124", 96),
    Student("Gleb Junior", "КН-124", 94),
]

with StudentCollectionCM(students_full) as collection:
    for student in collection:
        print(student)
        try:
            student.grade = 120
        except ValueError as e:
            print("Error:", e)

print()
print("What do we see: iteration, context manager and validation work together")
print("Why does it work: all protocols (__iter__, __next__, __enter__, __exit__, descriptor) are combined")
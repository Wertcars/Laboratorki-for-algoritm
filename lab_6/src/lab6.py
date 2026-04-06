from Student import Student


print("Task A - Define the Student class")
print()

stu_1 = Student("Nikita", "KH-134", 79.8)

print("Name:", stu_1.name)
print("Group:", stu_1.group)
print("Average grade:", stu_1.average_grade)

print("-------------------------------------------------")


print("Task B - Inspect internal structure")
print()

print("Original stu_1 __dict__:", stu_1.__dict__)

stu_1.__dict__["average_grade"] = 96.0

print("Modified stu_1 __dict__:", stu_1.__dict__)
print("Updated average_grade:", stu_1.average_grade)

print("-------------------------------------------------")


print("Task C - Implement __str__")
print()

print(stu_1)

print("-------------------------------------------------")


print("Task D - Implement __repr__")
print()

print(repr(stu_1))

print("-------------------------------------------------")


print("Task E - Implement equality (__eq__)")
print()

stu_2 = Student("Edward", "KH-52", 88.7)
stu_3 = Student("Nikita", "KH-134", 96.0)

print(f"stu_1 - {stu_1}")
print(f"stu_2 - {stu_2}")
print(f"stu_3 - {stu_3}")
print()

print("Result of stu_1 == stu_2:", stu_1 == stu_2)
print("Result of stu_1 == stu_3:", stu_1 == stu_3)
print("Result of stu_1 == 10:", stu_1 == 10)

print("-------------------------------------------------")


print("Task F - Implement ordering (__lt__)")
print()

try:
    print("stu_1 < stu_2:", stu_1 < stu_2)
    print("stu_2 < stu_1:", stu_2 < stu_1)
    print()

    print("try: stu_1 < 5")
    print(stu_1 < 5)
except TypeError as e:
    print("Error:", e)

print("-------------------------------------------------")


print("Task G - Sorting")
print()

students = [
    Student("Edward", "KH-52", 88.7),
    Student("Nikita", "KH-134", 96.0),
    Student("Kiril", "KH-125", 60.0),
]

print("Before sorting:")
for s in students:
    print(s)
print()

students.sort()

print("After sorting:")
for s in students:
    print(s)

print("-------------------------------------------------")
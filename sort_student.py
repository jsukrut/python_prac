python_students = [
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Akriti', 41],
        ['Harsh', 39]
]

second_highest = sorted(set([ marks for name, marks in python_students]))[1]
students = sorted([ name for name, marks in python_students if marks == second_highest])
for student in students:
    print(student)

rounded = round(8.8, 2)
print(rounded)

formatted = "{:.3f}".format(9.999)
print(formatted)
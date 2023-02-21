# list comprehension = a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read

# list = [1. expression 2. for item in iterable ]
# list = [1. expression 2. for item in iterable 3. if conditional]
# list = [1. expression 2. (if/else) 3. for item in iterable]

# 1...............
squares = []  # create an empty list
for i in range(1, 11):  # (for) => create a for loop
    # (expression) => define what each loop iteration should do
    squares.append(i * i)
print(squares)

square = [i*i for i in range(1, 11)]
print(square)

# 2.......
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

process = [i for i in students if i >= 60]
print(process)

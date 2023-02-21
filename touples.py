# tupile = collection which is ordered and unchangeable (immutable)
# used to group together related data
# used () instead of [] used in lists


student = ("Bro", 21, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")

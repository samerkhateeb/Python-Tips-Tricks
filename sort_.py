# sort () method = used with lists
# sort function = used with iterables

# list of touples
# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78)
#             ]

# # order = lambda x:x[1]
# def order(x): return x[1]
# students.sort(key=order, reverse=True)
# for i in students:
#     print(i)


# touple of touples

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)
            )


# # order = lambda x:x[1]
def order(x): return x[1]


new_sttudent = sorted(students, key=order)

for i in new_sttudent:
    print(i)

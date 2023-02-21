import os

source = "test.txt"

destination = "move/test.txt"

try:
    if os.path.exists(destination):
        print("there's already  a fil there")
    else:
        os.replace(source, destination)
        print(source + ' was moved')

except FileNotFoundError:
    print(source + " was not found")

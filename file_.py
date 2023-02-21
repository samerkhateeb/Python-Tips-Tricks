

try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found : (")


text = "Have a nice day! See ya"

# append file
with open('test. txt', 'a') as file:
    file.write(text)

# write file
with open('test. txt', 'w') as file:
    file.write(text)

# read file
with open('test. txt', 'r') as file:
    file.write(text)

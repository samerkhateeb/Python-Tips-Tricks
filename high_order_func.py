# Higher Order Function = a function that either:
# 1. accepts a function as an argument or
# 2. returns a function
# (In python, functions are also treated as objects)

# 1......
def hello():
    print("Hello")


hi = hello
hello()
hi()

say = print
say("Whoa! I can't believe this works! :0")


# 2......
def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))


# exception = events detected during execution that interrupt the flow of a program
#

try:
    numerator = int(input("'Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong : (")
else:  # it will execute only if there's no exception
    print(result)
finally:  # it will execute always
    print("This will always execute")

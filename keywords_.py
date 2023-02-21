# Keyword arguments = arguments preceded by an identifier when we pass them to a function The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print('Hellow {} {} {}'.format(first, middle, last))
    print('Hellow {f} {m} {l}'.format(f=first, m=middle, l=last))


hello(first='samer', middle='abed', last='kh')

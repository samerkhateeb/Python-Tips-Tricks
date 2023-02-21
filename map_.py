# тар () = applies a function to each item in an iterable (list, tuple, etc.)
#
# # map (function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# to_euro = lambda x:(x[0],x[1]*0.86)


def to_euro(x): return (x[0], x[1]*0.86)


store_euro = list(map(to_euro, store,))

for i in store_euro:
    print(i)

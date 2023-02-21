# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "Samer Alkhatib"
# slice from index 0 till index 3
first_name = name[: 3]
# slice from index4 till the end
last_name = name[4:]
# it will take every second character
funky_name = name[:: 3]

# reverse the name
reverse_name = name[::-1]

print(funky_name)
print(reverse_name)


websitel = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(websitel[slice])
print(website2[slice])

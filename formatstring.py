# str. format () = optional method that gives users more control when displaying output

name = "Bro"

print("Hello, my name is {}".format(name))

# => give space after {} with 10 digits
print('Hello, my  name is {:10}, nice to meet you'.format(name))
print('Hello, my  name is {:<10}, nice to meet you'.format(name))
print('Hello, my  name is {:>10}, nice to meet you'.format(name))
print('Hello, my  name is {:^10}, nice to meet you'.format(name))

number = 1000

print('the number pi is {:.3f}'.format(number))  # only 3 digits after the .
print('the number pi is {:,}'.format(number))  # comma every one thousand
print('the number pi is {:b}'.format(number))  # binary
print('the number pi is {:o}'.format(number))  # octet
print('the number pi is {:x}'.format(number))  # hex small
print('the number pi is {:X}'.format(number))  # hex cap
print('the number pi is {:e}'.format(number))  # Scientific Noation
print('the number pi is {:E}'.format(number))  # Scientific Noation

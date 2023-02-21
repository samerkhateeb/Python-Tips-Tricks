# thread = a flow of execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency
# GIL = (global interpreter lock),
#        allows only one thread to hold the control of the Python interpreter at any one time
# # cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#               use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#              use multithreading


import threading
import time


def eat_breadkfast():
    time.sleep(3)
    print('You eat coffee')


def drink_coffee():
    time.sleep(4)
    print('You drank coffee')


def study():
    time.sleep(5)
    print('You finish studying')

# sequential
# eat_breadkfast()
# drink_coffee()
# study()


# threading

x = threading.Thread(target=eat_breadkfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# thread syncronization: if we added this, the main thread will not execute before the threads , add this:
x.join()
y.join()
z.join()

# we have always main thread to execute the program
print(threading.active_count())
print(threading.enumerate())  # print list of  all the threads
print(time.perf_counter())  # check how much time it took

# daemon thread = a thread that runs in the background, not important for program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non-daemon threads cannot normally be killed, stay alive until task is complete
#                   ex. background tasks, garbage collection, waiting for input, long running processes


import threading
import time


def timer():
    print()
    count = 0

    while True:
        time.sleep(1)
        count += 1
        print(f"logged in for :{count} seconds")


# background timer still going but main thread is complete
# the program will not be killing as long non-daemon thread still alive
# when we make the daemon thread, the program will be killed when the thread is finished.
x = threading.Thread(target=timer, daemon=True)

x.start()  # after this the main  thread will complete

# x.setDaemon(True)  #another way to change to daemon thread, but cannot change it to daemon while it is running (means after x.start())
# print(x.isDaemon())

# when we type,  the timer stopped, so the daemon will be killed
# because all daemons are killed when the program stoopped running
answer = input("Do you wish to exit?")

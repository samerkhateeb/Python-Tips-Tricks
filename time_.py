import time
# ******************大*大******大*******************大*大*****大*大**********************************
print(time.ctime(0))
# convert a time expressed in seconds since epoch to a readable string
#                   epoch = when your computer thinks time began(reference point)
print(time.time())
# return current seconds since epoch
print(time.ctime(time.time()))  # will get current time

# **********************************************************************
# time.strftime (format, time_object) = formats a time_object to a string
# time_object = time. localtime () # local time
# time_object = time. gmtime () # UTC time
# local_time = time. strftime ("%B %d %Y %H: %M:%S", time _object)
# print (local_time)


# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

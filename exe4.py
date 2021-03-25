import time         #import the time module
print("*****TIME*****")
seconds = time.time() #The time() function returns the number of seconds passed since epoch.
print("Seconds since epoch =", seconds)
print("\n")
print("*****CURRENT TIME*****")
local_time = time.ctime(seconds) #The time.ctime() function takes seconds passed since epoch as an argument and returns a string representing local time.
print("Local time:", local_time)
print("\n")
print("This is printed immediately.")
time.sleep(2.4)   #The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
print("This is printed after 2.4 seconds.")
print("\n")
print("*****LOCAL TIME*****")
result = time.localtime(seconds) #The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("\n")
print("*****TIME AND HOUR*****")
result = time.gmtime(seconds)  #The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("\n")
print("*****MAKE TIME*****")
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
local_time = time.mktime(t) #The mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns the seconds passed since epoch in local time. Basically, it's the inverse function of localtime().
print("Local time:", local_time)
print("\n")
print("*****TIME WITH DAY*****")
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
result = time.asctime(t) #The asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument and returns a string representing it
print("Result:", result)
print("\n")
print("*****MONTH/DATE/YEAR*****")
named_tuple = time.localtime() # get struct_time 
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)#The strftime() function takes struct_time (or tuple corresponding to it) as an argument and returns a string representing it based on the format code used.
print(time_string)
print("\n")
print("*****TIME AS STRUCTURE FORMAT*****")
time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y") #The strptime() function parses a string representing time and returns struct_time.
print(result)
print("\n")

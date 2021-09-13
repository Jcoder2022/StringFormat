# let us say we want to display message like 'john [Smith] is a coder
first_name="John"
last_name='Smith'
message = first_name + " [" +last_name+ "] " + "is a coder"
print(message)
# Better approch is to use string formatter

msg = f'{first_name} [{last_name}] is a coder'
print(msg)

# String methods
course = "Python for Beginners"
# To calculate number of characters in string, use built in function called len()
print(len(course))
# len() is general purpose function, can be used to count items in list
# len() and print() function does not belong to string where as upper() method, lower belong to string
print(course.upper())
print(course.lower())
# find method - will return index of character's first occurrence in a string - it is case sensitive
print(course.find('y'))
print(course.find('O')) # will return -1, as its case sensitive
print(course.find('Beginners')) # will return 11,

# replace method
print(course.replace('Beginners',"Absolute Beginners"))

# in operator - to find if string contains particular word it returns True if it contains
print('Python' in course)
print('Jython' in course)

# difference between find and in
# find returns index of operator whereas in operator returns boolean value


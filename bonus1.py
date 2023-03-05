# Task 1: Write a program that will print the following to the console using the print() function

#rows = 8
#for row in range(0, rows):
#    for column in range(row):
#        print('#', end='')
#    print('')

# ✨ my personal notes ✨
# To define rows and columns in python to print patterns, you need to use a nested loop.
# The outer loop iterates the number of rows. 
# The inner loop iterates the number of columns.

# Task 2: Write a program that will print the following to the console using the print() function.

#for x in range(8):
#    if (x % 2 ==  0):
#        print(' # # # #')
#    else:
#        print('# # # # ')


# Task 3: Write a program that takes a number as input from the user, counts all of the digits in that number, and prints the digit count to the console.
# Example: Typing 53895 will print 5 to the console
# explanation: https://www.programiz.com/python-programming/examples/number-of-digits

number = input('Please enter any number for Python to count: ')
count = 0

# while number != 0:
#     number //= 10
#     count += 1
# print('Number of digits: ' + str(count))

# ORRRR 

print(len(str(number)))

# ✨ len() can be used with string or arrays


# Task 4: Find the factorial of a given number. A factorial means to multiply all of the numbers of a given number counting down to 1. For example, given the number 5, multiply 5 * 4 * 3 * 2 * 1 to get the result: 120.
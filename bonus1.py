# Task 1: Write a program that will print the following to the console using the print() function

#rows = 8
#for row in range(0, rows):
#    for column in range(row):
#        print('#', end='')
#    print('')

# To define rows and columns in python to print patterns, you need to use a nested loop.
# The outer loop iterates the number of rows. 
# The inner loop iterates the number of columns.

# Task 2: Write a program that will print the following to the console using the print() function.

for x in range(8):
    if (x % 2 ==  0):
        print(' # # # #')
    else:
        print('# # # # ')
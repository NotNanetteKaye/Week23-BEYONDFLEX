# Task 1: Write a program that will print the following to the console using the print() function

rows = 8
for row in range(0, rows):
    for column in range(row):
        print('#', end='')
    print('')
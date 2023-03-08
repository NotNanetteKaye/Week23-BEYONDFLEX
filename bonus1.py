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

# number = input('Please enter any number for Python to count: ')
# count = 0

# while number != 0:
#     number //= 10
#     count += 1
# print('Number of digits: ' + str(count))

# ORRRR 

# print(len(str(number)))

# ✨ len() can be used with string or arrays


# Task 4: Find the factorial of a given number. 
# A factorial means to multiply all of the numbers of a given number counting down to 1. For example, given the number 5, multiply 5 * 4 * 3 * 2 * 1 to get the result: 120.
# explanation: https://www.google.com/search?sxsrf=AJOqlzW7zQng87_IFaQFy1bFlBW5xe_Arg:1677990652373&q=how+to+find+factorial+of+a+number+in+python&tbm=vid&sa=X&ved=2ahUKEwiDlZWm-sP9AhWBlmoFHX7XBDkQ0pQJegQICxAB&biw=1080&bih=779&dpr=2#fpstate=ive&vld=cid:1b77bf9f,vid:-qPu96nQOSk

# number = int(input('enter the number: '))
# factorial = 1

# if (number < 0):
#    print('Cannot find factorial of negative numbers')
#elif (number == 0 or number == 1):
#    print('{}! = {}'.format(number, factorial))
#else:
#    for num in range(number, 1, -1):
#        factorial = factorial * num
#    print('the factorial for', number, 'is', factorial )

# Task 5: Write a program that will allow a user to play a “guess the number” game. This program should only allow the user five guesses to guess the correct number, and display messages for the three following cases:
# A correct guess (which should end the program)
# An incorrect guess, but there are still guesses left
# An incorrect guess, but there are no more guesses left and the program is over. This should also display the correct number to the user
# BONUS: Offer a “hint” after three wrong guesses (could be a range of numbers that the number falls within, for instance)
# BONUS: Generate the number randomly every time the program runs.
# explanation: https://www.google.com/search?sxsrf=AJOqlzVPqi-U27maG-ryUQYNoGFHBCvIrg:1677992892842&q=Write+a+program+that+will+allow+a+user+to+play+a+%E2%80%9Cguess+the+number%E2%80%9D+game.+This+program+should+only+allow+the+user+five+guesses+to+guess+the+correct+number,+and+display+messages+for+the+three+following+cases:&tbm=vid&sa=X&ved=2ahUKEwia0MDSgsT9AhUmmmoFHWPqCEoQ0pQJegQIBxAB&biw=1080&bih=779&dpr=2#fpstate=ive&vld=cid:5fa4dcc5,vid:Jk3az4ZXEKU

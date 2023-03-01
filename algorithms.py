# Task 1: Even or Odd
# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

number = int(input('Please enter a number: '))
if (number % 2 == 0):
    print(number, ' is an even number')
else:
    print(number, ' is an odd number')
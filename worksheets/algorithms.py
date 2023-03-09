# Task 1: Even or Odd
    # Given a numeric value, determine if it is even or odd.
    # The function should take the value in as a parameter and return a boolean value (True if even, False if odd).
    # Leave a comment above the function stating the time complexity.
    # Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# number = int(input('Please enter a number: '))
# if (number % 2 == 0):
#     print(number, ' is an even number')
# else:
#     print(number, ' is an odd number')


# Task 2: Less than 100
    # Given a list of numbers, determine if each item in the list is lower than 100.
    # The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than or equal to 100, True if all numbers are less than 100).
    # Leave a comment above the function stating the time complexity.
    # Send a screenshot of your solution and time complexity comment to your personal instructors chat.

# list_number = [4, 100, 40, 3]
# for number in list_number:
#     if number >= 100:
#         print('False, this value is greater than or equal to 100')
#     else:
#         print('True, this value is less than 100')

# Task 3: Repeated Names
    # Given a list of names, determine if any names are contained in the list more than once.
    # The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).

# names = ['Nani', 'Darling', 'Nani', 'Nanette']
# no_duplicate_names = set()
# duplicates = set(x for x in names if (x in no_duplicate_names or no_duplicate_names.add(x)))
# print(list(duplicates), 'is a duplicate name in names')
# print(list(no_duplicate_names), 'are all the names in list of names')


# Task 4: Sort List
    # Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method).
    # Suggested strategy:
        # Starting with the first two numbers, compare them to see which is larger. 
        # Place the lower number to the left and the higher number to the right.
        # Iterate through the list, checking each pair of numbers one at a time.
        # Repeat from the start until the entire list is sorted.

# The map() function in Python is a built-in function that applies a specified function to all the items in an iterable (e.g., a list) and returns an iterable map object (a map). The function is called with each item in the iterable as its argument, and the results are collected into a new iterable.

# The general syntax of the map() function is:
#map(function, 'iterable, ...')
# Here, function is the function to which each item of the iterable is passed, and iterable is one or more iterables whose elements are processed by the function.

# Let's dive into two examples to illustrate the use of the map() function:

# Example 1: Squaring Numbers
# Define a function to square a number

def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to square each number in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list and print the result
result = list(squared_numbers)
print(result)        #[1, 4, 9, 16, 25]



# In this example, the square() function is applied to each element in the numbers list using the map() function, resulting in a new list containing the squared values.

# Example 2: Converting Strings to Integers

# Define a function to convert a string to an integer
def string_to_int(s):
    return int(s)

# Create a list of strings representing numbers
string_numbers = ['1', '2', '3', '4', '5']

# Use map() to convert each string to an integer
integers = map(string_to_int, string_numbers)

# Convert the map object to a list and print the result
result = list(integers)
print(result) #[1, 2, 3, 4, 5]

# In this example, the string_to_int() function is applied to each element in the string_numbers list using the map() function, resulting in a new list containing the corresponding integers.

# The map() function is particularly useful when you need to apply a specific operation to each element in an iterable without writing an explicit loop.
# It provides a concise and readable way to transform data in a functional programming style.

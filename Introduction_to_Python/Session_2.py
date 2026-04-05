# --------------------------------------------------
# Session 2: Introduction to Python
# --------------------------------------------------
## Author: Chandan Chaudhari
## Github: https://github.com/chandanc5525
# --------------------------------------------------

# Asking user for input
name = input("Please enter your name: ")
print(f"Hello, {name}! Welcome to the world of Python programming.")

# --------------------------------------------------

# Concept of Slicing and Indexing in Python with String
string = "Hello, Welcome to the world of Python Programming"

# Indexing
print(string[0])   
print(string[-1])

# Slicing
''' 
string[start:stop:step]
- start: The starting index of the slice (inclusive).
- stop: The ending index of the slice (exclusive).
- step: The step size or the interval between characters in the slice (optional).
'''

print(string[0:5])
print(string[7:14])
print(string[::2])  # Every second character
print(string[::-1]) # Reversed string

# --------------------------------------------------

''' 
Exercise:
1. Ask the user to input a string and perform the following operations:
1. Extract the word "Welcome" from the string.
2. Extract the word "Python" from the string.
3. Extract every third character from the string.
4. Reverse the string using slicing.
'''
# --------------------------------------------------

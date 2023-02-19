# QUESTION 2

# What is going on here? Can you explain the output?

tup = "Hello"
print(len(tup))

# This returns "5"
# "Hello" is a string variable, thus len(tup) results in the length of the string

tup = "Hello",
print(len(tup))

# This returns "1"
# The trailing comma signifies "Hello" should be added to a tuple (no parenthesis required to create a tuple)
# len(tup) returns the number of tuple elements in the tuple

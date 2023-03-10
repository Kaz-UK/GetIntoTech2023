# Question 1:

# Write a line of code to create a file handle to open and append to a file called pelican.txt
open_file = open("pelican.txt", "a")

# Append the following line to the file using the write method of the file handle: "A wonderful bird is the pelican"
open_file.write("A wonderful bird is the pelican,\n")

# Append the following second line using the write method: "His bill holds more than his belican"
open_file.write("His bill holds more than his belican.\n")

# Create a list that contains the following lines:
# lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

# Append this list to the file using the writelines method
open_file.writelines(lines)

# Why are the "\n" required?
# \n required to initialise a carriage return after each element in the list, so they appear on separate lines in doc

open_file.close()

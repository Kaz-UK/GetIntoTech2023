# Question 2

# Use the open and read methods to slurp the entire contents of your pelican.txt file
open_file = open("pelican.txt", "r")
my_text = open_file.read()
# Display the type of the returned data and print the contents of the returned data
print(type(my_text))
print(my_text)
open_file.close()

# What data type is the output?
# my_text is string data type

# Write some code that will read the pelican.txt file into a list and then output the number of items within the list
pelican_list = open("pelican.txt").read().splitlines()
# Above splits into lines, but could have split into words
# pelican_list = open("pelican.txt").read().split()
print(pelican_list)
print(len(pelican_list))
open_file.close()

# Use a loop to iterate over and print the contents of the file. Be sure not to include any blank lines in the output
with open("pelican.txt", "r") as infile:
    for line in infile:
        print(line, end="")
# No need to close file, as it is automatically closed during the loop

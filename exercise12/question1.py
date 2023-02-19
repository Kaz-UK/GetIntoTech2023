# QUESTION 1

# What is wrong with this?

cheese = ["Cheddar", "Stilton", "Cornish Yarg"]
cheese += "Oke"

# Python needs a list identifier [] to turn the string into a list
# As cheese is a list it runs through the string "Oke" and turns every letter into an element, so the list becomes:
# ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']

# How should 'Oke' be added to the end of the cheese list?

cheese = ["Cheddar", "Stilton", "Cornish Yarg"]
cheese += ["Oke"]
# or:
# cheese.extend(["Oke"])
# cheese.append("Oke")

# How would you add two new cheeses to the list with a single command?
cheese += ["Danish Blue", "Yorkshire Blue"]
# or:
# cheese.extend(["Danish Blue", "Yorkshire Blue"])

print(cheese)

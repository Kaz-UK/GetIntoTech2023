# This calculator offers no checks on data entry, so incorrect data will result in an error

print("Welcome to My Basic Calculator\n")

print("Please note: This calculator will calculate integers and all calculations are done on the same operator\n")

start = "y"

while start.lower() == "y":
    numbers = input("Please enter your numbers, leaving a space between numbers (e.g. 4 14 24): ")
    operator = input("Select an operator from the following ( +, -, /, * ): ")

    # Changes the string into a list
    string_list = numbers.split(" ")

    # Changes the string into an integer list
    numbers_list = list(map(int, string_list))

    # Collects the first number in the numbers list to use as the first number [position 0] in the calculation
    result = numbers_list[0]

    # Starts the calculation using the second number [position 1] in the numbers list
    for num in range(1, len(numbers_list)):
        if operator == "+":
            result += numbers_list[num]
        elif operator == "-":
            result -= numbers_list[num]
        elif operator == "/":
            result /= numbers_list[num]
        else:
            result *= numbers_list[num]

    # Prints out the result
    print("The result is: " + str(result))

    # Asks user if we should continue the loop
    start = input("Press 'y' to continue, or any other key to quit: ")
else:
    print("Thank you for using My Basic Calculator")

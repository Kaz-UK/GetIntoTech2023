print("\n++++++++++++ WELCOME TO MY BASIC CALCULATOR ++++++++++++")

start = "y"

while start.lower() == "y":
    print("\nThis calculator can support the following functions\n")
    print("\tAddition (using the '+' key)")
    print("\tSubtraction (using the '-' key)")
    print("\tMultiplication (using the '*' key")
    print("\tDivision (using the '/' key)\n")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # Collect data for first number
    operator_list = []
    number_list = []
    first_number_pass = False
    while not first_number_pass:
        number = input("Please enter a number: ")
        try:
            first_number = float(number)
            first_number_pass = True
        except ValueError or NameError:
            print("\t** That was not a valid number! **")

    # Asks user if they would like to continue adding numbers
    additional_number = "y"
    while additional_number.lower() == "y":
        data_entry_operator_pass = False
        data_entry_number_pass = False
        while not data_entry_operator_pass:
            operator = input("Please enter an operator (+, -, *, /): ")
            if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                data_entry_operator_pass = True
                operator_list.append(operator)
            else:
                print("\t** That was not a valid operator! **")
        while not data_entry_number_pass:
            number = input("Please enter a number: ")
            try:
                number = float(number)
                number_list.append(number)
                data_entry_number_pass = True
            except ValueError or NameError:
                print("\t** That was not a valid number! **")
        additional_number = input("Type 'y' if you would like to add another number, or press any key to continue: ")

    # Calculates numbers with operators, using the first number to start the process
    calculation = first_number
    for number, operator in zip(number_list, operator_list):
        if operator == "+":
            calculation += number
        elif operator == "-":
            calculation -= number
        elif operator == "*":
            calculation *= number
        else:
            calculation /= number

    # Prints the answer
    print("The answer is: " + str(calculation))

    # Asks user if they wish to continue
    start = input("Type 'y' to conduct another sum, or press any other key to exit: ")
else:
    print("\nThank you for using My Basic Calculator")
    print("Last updated: 11 February 2023")

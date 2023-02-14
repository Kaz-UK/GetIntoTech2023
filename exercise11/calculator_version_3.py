# Calculator takes multiple numbers and operators and calculates them according to operator precedence
# But calculator uses eval, which is bad programming practice

print("\n++++++++++++ WELCOME TO MY BASIC CALCULATOR ++++++++++++")

start = "y"

while start.lower() == "y":
    print("\nThis calculator can support the following functions\n")
    print("\tAddition (using the '+' key)")
    print("\tSubtraction (using the '-' key)")
    print("\tMultiplication (using the '*' key")
    print("\tDivision (using the '/' key)\n")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # Captures first number and creates empty list for operators
    # First number is separated out to ensure data collection ends with a number, not operator
    calculation_list = []
    first_number_pass = False
    while not first_number_pass:
        number = input("Please enter a number: ")
        try:
            number = float(number)
            calculation_list.append(number)
            first_number_pass = True
        except ValueError or NameError:
            print("\t** That was not a valid number! **")
    user_continue = "y"

    # Collects operator and number data
    while user_continue.lower() == "y":
        data_entry_operator_pass = False
        data_entry_number_pass = False
        while not data_entry_operator_pass:
            operator = input("Please enter an operator (+, -, *, /): ")
            if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                data_entry_operator_pass = True
                calculation_list.append(operator)
            else:
                print("\t** That was not a valid operator! **")
        while not data_entry_number_pass:
            number = input("Please enter a number: ")
            try:
                number = float(number)
                calculation_list.append(number)
                data_entry_number_pass = True
            except ValueError or NameError:
                print("\t** That was not a valid number! **")
        user_continue = input("Press 'y' to add another number, or press any other key to continue: ")

    # I have used the eval function to evaluate the list as a string and execute if a legal Python statement
    # But eval should be used with caution as it is likely to create a security risk
    # In future I should avoid using eval in any code as it is considered insecure and bad programming practice
    result = eval(" ".join(str(data) for data in calculation_list))

    # Print the result of the calculation
    printout = format(" ".join(str(data) for data in calculation_list))
    print("\n\tThe result of your calculation:\n\t" + printout + " = " + str(result))

    # Ask user if they wanted to restart the process
    start = input("\nType 'y' to conduct another calculation, or press any other key to exit: ")

# End message as program exits
else:
    print("\nThank you for using My Basic Calculator")
    print("Last updated: 14 February 2023")

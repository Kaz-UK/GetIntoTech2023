print("************** Welcome to My Basic Calculator **************")
calculation_history = []
calculation_history_bool = False
calculator = "y"

while calculator.lower() == "y":
    print("""
    1. Perform a calculation
    2. View calculation history
    3. Exit calculator
    """)
    menu_choice = input("Please select an option: ")

    if menu_choice == "1":
        calculation_numbers = []
        number_pass = False
        operator_pass = False
        while not number_pass:
            numbers = input("Please enter your numbers, leaving a space between numbers (e.g. 4 14 24): ")
            string_list = numbers.split(" ")
            calculation_numbers = []
            try:
                for numbers in string_list:
                    valid_number = float(numbers)
                    calculation_numbers.append(valid_number)
                    number_pass = True
            except ValueError or NameError:
                print("\t*** That was not a valid number! ***")
                number_pass = False

        while number_pass is True and operator_pass is False:
            operator = input("Select an operator from the following ( +, -, /, * ): ")
            if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                operator_pass = True
            else:
                print("\t*** That was not a valid operator! ***")

        result = calculation_numbers[0]
        history = [str(calculation_numbers[0])]
        for num in range(1, len(calculation_numbers)):
            history.extend(" " + operator + " " + str(calculation_numbers[num]))
            if operator == "+":
                result += calculation_numbers[num]
            elif operator == "-":
                result -= calculation_numbers[num]
            elif operator == "/" and calculation_numbers[num] == 0:
                print("You cannot divide by zero and this number will be removed from the calculation")
            elif operator == "/":
                result /= calculation_numbers[num]
            else:
                result *= calculation_numbers[num]

        result_calculation = "".join(history) + " = " + str(result)
        calculation_history.extend([result_calculation])
        print("\n\tThe result: " + result_calculation)
        calculation_history_bool = True
        calculator = input("\nPress 'y' to return to the main menu, or any other key to exit: ")

    elif menu_choice == "2":
        if calculation_history_bool is not True:
            print("You have made no calculations")
        else:
            print("\n\tYour calculation history:")
            for history in calculation_history:
                print("\t" + history)
        calculator = input("\nPress 'y' to return to the main menu, or any other key to exit: ")

    elif menu_choice == "3":
        calculator = "n"

    else:
        print("\n\t*** Error: Please select a valid option from the menu ***")

else:
    print("Thank you for using My Basic Calculator")



def start_calculator():
    menu_choice = False
    menu_selection = ""
    print("""
    1. Perform a calculation
    2. View calculation history
    3. Exit calculator
    """)
    while not menu_choice:
        if menu_selection == "1" or menu_selection == "2" or menu_selection == "3":
            menu_choice = True
        else:
            menu_selection = input("Please select a valid option: ")
    return menu_selection


def collect_numbers():
    calculation_numbers = []
    number_pass = False
    while not number_pass:
        number_data_input = input("Please enter your numbers, leaving a space between numbers (e.g. 4 14 24): ")
        string_list = number_data_input.split(" ")
        calculation_numbers = []
        try:
            for number in string_list:
                valid_number = float(number)
                calculation_numbers.append(valid_number)
                number_pass = True
        except ValueError or NameError:
            print("\t*** That was not a valid number! ***")
            number_pass = False
    return calculation_numbers


def collect_operator():
    operator_pass = False
    while operator_pass is False:
        operator_input = input("Select an operator from the following ( +, -, /, * ): ")
        if operator_input == "+" or operator_input == "-" or operator_input == "*" or operator_input == "/":
            operator_pass = True
        else:
            print("\t*** That was not a valid operator! ***")
    return operator_input


def calculation(operator, numbers):
    answer = numbers[0]
    for num in range(1, len(numbers)):
        if operator == "+":
            answer += numbers[num]
        elif operator == "-":
            answer -= numbers[num]
        elif operator == "/" and numbers[num] == 0:
            print("You cannot divide by zero and this number was removed from the calculation")
        elif operator == "/":
            answer /= numbers[num]
        else:
            answer *= numbers[num]
    return answer


def result_printout_history(operator, numbers):
    archiving_result = [str(numbers[0])]
    for num in range(1, len(numbers)):
        archiving_result.extend(" " + operator + " " + str(numbers[num]))
    return archiving_result


def calculator_history(calc_history, calc_bool):
    if calc_bool is not True:
        print("You have made no calculations")
    else:
        print("\n\tYour calculation history:")
        for history_result in calc_history:
            print("\t" + history_result)


# Calculator program starts

print("************** Welcome to My Basic Calculator **************")
calculation_history_bool = False
execute_program = "y"
calculation_history = []

while execute_program.lower() == "y":

    # MAIN MENU
    verified_menu_choice = start_calculator()

    # MENU 1 - CALCULATOR
    if verified_menu_choice == "1":

        # Data collection (number(s) and operator)
        verified_numbers = collect_numbers()
        verified_operator = collect_operator()

        # result = verified_numbers[0]
        result = calculation(verified_operator, verified_numbers)

        # Create history
        history = result_printout_history(verified_operator, verified_numbers)
        result_calculation = "".join(history) + " = " + str(result)
        print("\n\tThe result: " + result_calculation)

        # Calculation history
        calculation_history.extend([result_calculation])
        calculation_history_bool = True
        execute_program = input("\nPress 'y' to return to the main menu, or any other key to exit: ")

    # MENU 2 HISTORY
    elif verified_menu_choice == "2":
        calculator_history(calculation_history, calculation_history_bool)
        execute_program = input("\nPress 'y' to return to the main menu, or any other key to exit: ")

    # MENU 3 EXIT CALCULATOR
    elif verified_menu_choice == "3":
        execute_program = "n"

else:
    print("Thank you for using My Basic Calculator")

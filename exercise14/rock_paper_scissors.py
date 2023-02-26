# OBJECTIVE
# To practice creating functions
# To revisit conditional structures
# To use built-in functions
# CREATE A GAME: ROCK, PAPER, SCISSORS!
# You are going to create a command line version of the game: Rock...Paper...Scissors!
# The user will play against the computer at this game. You should design a program that does the following:
# * Prompts the user to enter a value: R, P or S
# * The program should convert this value into Rock, Paper, or Scissors respectively
# * Asks the computer to generate a random value between 0 and 2
# * Converts the computer's choice. 0 becomes Rock, 1 becomes Paper, 2 becomes Scissors
# * Compare the user's choice with the computer's choice to display a message indicating whether the user won, lost
#   drew against the computer
# * Showcase what you have learned about conditional statements and create your own functions

# Import randint to allow the computer to make a selection
from random import randint

# Program functions


def game_rules():
    print("""
    GAME RULES
    Rock crushes Scissors
    Paper covers Rock
    Scissors cuts Paper
    
    Best of 3 wins!
    """)


def user_input():
    input_check = "N"
    valid_inputs = ["R", "P", "S"]
    while input_check.upper() not in valid_inputs:
        input_check = input("Please select an option (R, P, S): ")
    else:
        return input_check.upper()


def computer_input():
    computer_select = randint(0, 2)
    return computer_select


def conversion(selected_option):
    if selected_option == "R" or selected_option == 0:
        confirmed_input = "Rock"
    elif selected_option == "P" or selected_option == 1:
        confirmed_input = "Paper"
    elif selected_option == "S" or selected_option == 2:
        confirmed_input = "Scissors"
    return confirmed_input


def contest(user, computer):
    if user == "Rock":
        if computer == "Scissors":
            game_result = "Win"
            print("** You win! Rock crushes Scissors **")
        elif computer == "Paper":
            game_result = "Loss"
            print("** You lose! Paper covers Rock **")
        else:
            game_result = "Draw"
    elif user == "Paper":
        if computer == "Rock":
            game_result = "Win"
            print("** You win! Paper covers Rock **")
        elif computer == "Scissors":
            game_result = "Loss"
            print("** You lose! Scissors cuts Paper **")
        else:
            game_result = "Draw"
    elif user == "Scissors":
        if computer == "Paper":
            game_result = "Win"
            print("** You win! Scissors cuts Paper **")
        elif computer == "Rock":
            game_result = "Loss"
            print("** You lose! Rock crushes Scissors **")
        else:
            game_result = "Draw"
    return game_result


def score(existing_game_score, current_game):
    if current_game == "Win":
        existing_game_score[0] += 1
    elif current_game == "Loss":
        existing_game_score[1] += 1
    else:
        print("A draw, so no change in the score!")
    print("\n** User: {} ** Computer: {} **\n".format(existing_game_score[0], existing_game_score[1]))
    return existing_game_score


def winner(existing_game_score):
    if existing_game_score[0] == 2:
        print("** CONGRATULATIONS, YOU HAVE WON THE MATCH! **\n")
    elif existing_game_score[1] == 2:
        print("** COMPUTER WINS THE MATCH, BETTER LOOK NEXT TIME! **\n")


def play_again():
    continue_game = input("Play again? Press 'Y' to continue or any other key to exit: ")
    return continue_game


# PROGRAM STARTS
print("******* Welcome to this game of Rock, Paper, Scissors *******")
game_rules()
execute_program = "Y"

while execute_program.upper() == "Y":

    # Starts game at zero, resetting game score from any previous game
    game_score = [0, 0]

    while 2 not in game_score:

        # Obtain the user input
        user_selection = user_input()

        # Convert the user input to Rock, Paper or Scissors
        confirmed_user_choice = conversion(user_selection)
        print("You chose:", confirmed_user_choice)

        # Obtain the computer input
        computer_selection = computer_input()

        # Convert the computer input to Rock, Paper or Scissors (using same function as used for user input)
        confirmed_computer_choice = conversion(computer_selection)
        print("The computer chose:", confirmed_computer_choice)

        # Execute game (loops until one player has 2 wins)
        result = contest(confirmed_user_choice, confirmed_computer_choice)
        score(game_score, result)
        winner(game_score)

    else:
        execute_program = play_again()

else:
    print("Thank you for playing!")

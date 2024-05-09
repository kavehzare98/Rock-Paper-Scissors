# flow control
# Rock, Paper, Scissors - my version
from RPS_game_functions import *
def main():

    # set game_flag = True
    game_flag = True

    # While Loop for game
    while game_flag == True:

        # Call makeComputerChoice() function
        computer_choice = makeComputerChoice()

        # Call takeUserInput() function
        user_input = takeUserInput()

        valid_input, user_choice = validateUserInput(user_input)

        while valid_input == False:
            user_input = takeUserInput()
            valid_input, user_choice = validateUserInput(user_input)

        # Call determineWinner(computer_choice, user_choice) function
        determineWinner(computer_choice, user_choice)

        # Call playAgain() function and check for output
        if playAgain().lower() == 'n':
            game_flag = False

    # End of Program

main()
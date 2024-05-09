import random
from RPS_ASCII_art import *  # Assuming RPS_ASCII_art contains ASCII art for the game choices

# Create choice list
choice_list = ["rock", "paper", "scissor"]


# This function will use the random module to make a choice for the computer and returns the choice
def makeComputerChoice():
    """
    Randomly selects a choice for the computer.

    Returns:
        str: The choice selected for the computer.
    """
    choice = random.choice(choice_list)
    return choice


# This function only prompts the user and accepts user input
def takeUserInput():
    """
    Prompts the user to input their choice for the game (rock, paper, or scissors).

    Returns:
        str: The user's input as a string.
    """
    user_input = input("Please enter a valid choice option:\n1 - Rock\n2 - Paper\n3 - Scissor\n\nYour Choice:\t")
    return user_input


# This function assumes that the user_input is valid unless it falls outside of choice range or a letter or phrase is
# entered instead.
def validateUserInput(user_input):
    """
    Validates the user's input to ensure it is a valid choice for the game.

    Parameters:
        user_input (str): The user's input received from takeUserInput().

    Returns:
        tuple: A tuple containing a boolean value indicating whether the input is valid
               and the user's choice (if valid).
    """
    valid_input = True
    try:
        user_choice = int(user_input)
        if (user_choice < 1) or (user_choice > 3):
            print("You entered an invalid number! Please try again.")
            valid_input = False
        user_choice -= 1
    except ValueError:
        print("Invalid input!")
        valid_input = False
        user_choice = None
    return valid_input, user_choice


# This function takes two inputs: one from the computer and one from the user
def determineWinner(computer_input, user_choice):
    """
    Determines the winner of the game based on the choices made by the computer and the user.

    Parameters:
        computer_input (str): The choice made by the computer.
        user_choice (int): The choice made by the user.
    """
    print('\n', art_list[user_choice], sep='')
    print('\n', art_list[choice_list.index(computer_input)], sep='', end='\n\n')

    if computer_input == "rock":
        if choice_list[user_choice] == "paper":
            print(f"User wins! {choice_list[user_choice]} beats {computer_input}")
        elif choice_list[user_choice] == "scissor":
            print(f"Computer wins! {computer_input} beats {choice_list[user_choice]}")
        else:
            print("It's a tie!")
    elif computer_input == "paper":
        if choice_list[user_choice] == "scissor":
            print(f"User wins! {choice_list[user_choice]} beats {computer_input}")
        elif choice_list[user_choice] == "rock":
            print(f"Computer wins! {computer_input} beats {choice_list[user_choice]}")
        else:
            print("It's a tie!")
    elif (computer_input == "scissor"):
        if choice_list[user_choice] == "rock":
            print(f"User wins! {choice_list[user_choice]} beats {computer_input}")
        elif choice_list[user_choice] == "paper":
            print(f"Computer wins! {computer_input} beats {choice_list[user_choice]}")
        else:
            print("It's a tie!")


# Function to prompt the user if they want to play again
def playAgain():
    """
    Prompts the user to decide whether they want to play the game again.

    Returns:
        str: The user's decision to play again as a string ('Y' or 'N').
    """
    play_again = input("\nWould you like to play again (Y or N)?\t")
    while (play_again.lower() != 'y') and (play_again.lower() != 'n'):
        print("Invalid entry!")
        play_again = input("\nWould you like to play again (Y or N)?\t")
    return play_again

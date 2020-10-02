"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random


def start_game():
    
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """

    # prompting the users Name
    #greeting the user to the Game
    name_1 = input("Please enter your name.   ")
    print(name_1)
    welcome = ("Welcome {}, to the Guessing game!!!".format(name_1))
    # prompting the user if the user would like to play the Game
    # if the user uses an int the for loop would activate
    # if the user does not enter 'y' or 'Y' the user would be exited out of the Game
    # if the user enters 'y' or 'Y' the user would be entered in the game
    try:
        play = input("Would you like to play the Guessing game {}? (Yes/No only)  ".format(name_1))
        while play.isnumeric():
            play = input("Would you like to play the Guessing game {}? (Yes/No only)  ".format(name_1))
    except (ValueError, TypeError):
        print("Please enter (Yes or No only) not {}.".format(play))
    else:
        if play.lower() != "y":
            print("GoodBye {}!".format(name_1))
            quit()
    
    
    now = ("Let the Games Begin!!")
    num = ("The rules are to guess between 1-10")
    print(welcome)
    print(now)
    print(num)
    # everything will be used if it is True using the while loop
    while True:
    # creating a variable to hold the min and the max of the guessing game.
    # using a variable to enter the tries
    # using a variable to store the guesses of the user
        solution = random.randint(1, 10)
        tries = 0
        guess = -1
    
    # prompting the user to pick a number
        guess = input("Pick a number:  ")
        guess = int(guess)
    
    # if too low or too high the user will be prompted to go lower or higher
        while guess != solution:
            if guess < solution:
                print("{} is too low!".format(guess))
                guess = int(input("Try again. "))
                tries = tries + 1
            elif guess > solution:
                print("{} is too high!".format(guess))
                guess = int(input("Try again. "))
                tries = tries + 1
        tries = tries + 1
        try:
            print("Congrats {} {} was the random number! You Won The Guessing Game! You had {} guesses!".format(name_1, guess, tries))
            play_again = input("Would you want to play again? (Yes/No):  ")
            while play_again.isnumeric():
                play_again = input("Would you want to play again? (Yes/No):  ")
        except (ValueError, TypeError, NameError):
                play_again = input("Would you want to play again? (Yes/No):  ")
    
        else:
            if play_again.lower() != "yes":
                print("See you later {}!".format(name_1))
                quit()
        print(play_again)
        print("Alright another round {}.".format(name_1))
    # show the user the tries and what the right guess was
    # congrats the user for finishing the game
    # prompt the user to play again
    # if the user uses any other str the user will be exited out of the game
    # prompt the user back the play again question if int is used
    # prompt the user ValueError, TypeError, NameError is made to play again question
start_game()
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
            play = input("Please enter (Yes/No only), {}!  ".format(name_1))
    except (ValueError, TypeError):
        print("Please enter (Yes or No only) not {}.".format(play))
    else:
        while play.lower() != "yes":
            try:
                if play.lower() == "no":
                    print("Maybe you can play next time! Goodbye, {}!!".format(name_1))
                    quit()
                play = input("Please enter (Yes/No only), {}!  ".format(name_1))
            except (ValueError, TypeError):
                print("Please enter (Yes or No only) not {}.".format(play))
            else:
                if play == "no":
                    print("Maybe you can play next time! Goodbye, {}!!".format(name_1))
                    quit()


    now = ("""Let the Games Begin!!


          """)
    num = ("""
           !!!The rules are to guess between the minimum and the maximum number that the user will give!!!

          """)
    error = ("""     !!!If the user enters a non number on the min, max, and the guess questions the game will restart!!!

    """)

    print(welcome)
    print(num)
    print(error)
    print(now)
    # everything will be used if it is True using the while loop
    while True:
    # creating a variable to hold the min and the max of the guessing game.
    # using a variable to enter the tries
    # using a variable to store the guesses of the user

    # prompting the user to pick a number




    # if too low or too high the user will be prompted to go lower or higher
        try:
            maximum = int(input("Give me a max number!   "))
            minimum = int(input("Give me a min number!   "))
            guess = input("Pick a number:  ")
        except (ValueError, TypeError, NameError):
            print("The game will now restart")
            start_game()
        else:
            minimum = int(minimum)
            maximum = int(maximum)
            guess = int(guess)
            solution = random.randint(minimum, maximum)
            tries = 1
            while guess != solution:
                if guess < solution:
                    print("{} is too low!".format(guess))
                    guess = int(input("Try again. "))
                    tries = tries + 1
                elif guess > solution:
                    print("{} is too high!".format(guess))
                    guess = int(input("Try again. "))
                    tries = tries + 1
                highscore = tries
            try:
                print("Congrats {} {} was the random number! You Won The Guessing Game! You had {} guesses!".format(name_1, guess, tries))
                print("Your Highscore is {}!!!".format(highscore))



                play_again = input("Would you want to play again? (Yes/No):  ")
                while play_again.isnumeric():
                    print("Please enter (Yes/No only)")
                    play_again = input("Would you want to play again? (Yes/No):  ")
            except (ValueError, TypeError, NameError):
                    play_again = input("Would you want to play again? (Yes/No):  ")

            else:
                while play_again.lower() != "yes":
                    try:
                        if play_again.lower() == "no":
                            print("See you later {}!".format(name_1))
                            quit()
                        print("Please enter (Yes/No only)")
                        play_again = input("Would you want to play again? (Yes/No):  ")
                    except (ValueError, TypeError, NameError):
                            play_again = input("Would you want to play again? (Yes/No):  ")
                    else:
                        if play_again == 'no':
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

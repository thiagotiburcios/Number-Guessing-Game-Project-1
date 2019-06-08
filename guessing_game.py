import random


def start_game():

    print(" ******** WELCOME TO THE GUESSING GAME *********** \n ")

    answer_solution = random.randint(1, 10)
    picks = -1

    highscore = None

    play_again = "y"

    while play_again == "y":

        current_score = 0
        while picks != answer_solution:
            try:

                picks = input("\nPlease, pick a number between 1 and 10: ")
                picks = int(picks)

                if picks in range(1, 10):
                    current_score += 1

                    if picks > answer_solution:
                        print("It is lower!")
                    if picks < answer_solution:
                        print("It is higher!")
                else:
                    print("Sorry, number {}, is outside the range [1 to 10]".format(picks))

            except ValueError:
                print("Sorry, number must be in numeral. Please try again...")

        else:
            print("""\nWell done! You got it. 
            \nIt took you {} times.""".format(current_score))
            if highscore is None:
                highscore = current_score
            elif current_score < highscore:
                highscore = current_score
            play_again = input("\nWould you like to play again? [y]es or [n]o  ")
            picks -= 1

            print("\n***** The HIGHSCORE is: {} *****".format(highscore))

    print("\nCLOSING GAME! \nThanks for playing, see you next time!")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()



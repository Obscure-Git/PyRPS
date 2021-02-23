import random  # for letting the computer make a random choice out of [r, p, s]
import math  # for math.ceil() function

play_msg = (
    "\nWhat is your play? 'r' for Rock , 'p' for paper and 's' for scissors.\n>> "
)

times_to_play_msg = (
    "How many times do you want to play? (* Provide a whole number)\n>> "
)

times_to_play = input(times_to_play_msg)

# The loop will keep asking for new input until its a valid input
while times_to_play.isdigit() == False:
    print("Please provide a number.")
    times_to_play = input(times_to_play_msg)

times_to_play = int(times_to_play)


def results():
    player = input(play_msg)  # Getting input from the player.

    # The loop will keep asking for new input until its a valid input
    while player.isdigit() == True:
        print("Please provide an english alphabet not an integer.")
        player = input(play_msg)

    player = player.lower()  # Converting the player input to lowercase.

    computer = random.choice(["r", "p", "s"])

    if player != "r" and player != "p" and player != "s":
        return -1

    if player == computer:
        return (0, player, computer)

    # r > s, s > p, p > r
    if winner(player, computer):
        return (1, player, computer)

    return (2, player, computer)


def winner(winner, loser):

    if (
        (winner == "r" and loser == "s")
        or (winner == "s" and loser == "p")
        or (winner == "p" and loser == "r")
    ):
        return True

    return False


def play(num):
    player_pts = 0
    computer_pts = 0

    required_pts_to_win = math.ceil(
        num / 2
    )  # the provided number is divided by half and the math.ceil() function rounds the number up to the next largest integer. Example : if given number is 5 the division returns 2.5 which rounds up to 3.

    # keeps running the below code if required pts to win has not been achieved by any of the player.
    while player_pts < required_pts_to_win and computer_pts < required_pts_to_win:
        result, player, computer = results()

        # Case : Invalid Option Chosen
        if result == -1:
            print("Invalid Option.")

        # Case : Tie
        elif result == 0:
            print("\nIt's a tie.")

        # Case : Player Win
        elif result == 1:
            player_pts += 1  # player_pts = player_pts + 1
            print(
                "\nYou won! You chose {} and computer chose {}".format(player, computer)
            )

        # Case : Computer wins
        elif result == 2:
            computer_pts += 1  # computer_pts = computer_pts + 1
            print(
                "\nYou lost! You chose {} and computer chose {}".format(
                    player, computer
                )
            )

    # Checking who won the most number of games.
    if player_pts > computer_pts:
        print("\nYou won the best of {} game against Computer!".format(num))

    else:
        print("\nYou lost the best of {} game against Computer!".format(num))

    # Asking to play again
    play_again = input("Do you want to play again? 'y' for yes, 'n' for no.")

    # The loop will keep asking for new input until its a valid input
    while play_again.isdigit() == True:
        print("Please choose a valid option. 'y' for yes and 'n' for no.")
        play_again = input("Do you want to play again? 'y' for yes, 'n' for no.")

    # Rerunning the game if they want to play
    if play_again == "y":
        times_to_play = input(times_to_play_msg)

        # The loop will keep asking for new input until its a valid input
        while times_to_play.isdigit() == False:
            print("Please provide a number.")
            times_to_play = input(times_to_play_msg)

        times_to_play = int(times_to_play)

        play(times_to_play)  # Playing again if a number is provided.

    elif play_again == "n":
        print(
            "Thank you for playing!"
        )  # This message will be shown if they dont play again.


# Running the game // if statement is optional
if __name__ == "__main__":
    play(times_to_play)
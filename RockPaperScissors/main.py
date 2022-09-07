import random


def play():

    '''
    Method that is being called to play the game
    Takes input from user
    Randomly selects inpur for the computer
    Determines who won

    '''

    user = str(input("Enter 'r' for rock, 'p' paper, 's' for scissors:\t"))
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a Tie! Try again."
    elif IsWin(user, computer):
        return "You win! Congrats."

    return "Computer Won! Try again"


def IsWin(player, opponent):

    '''

    Returns True if the player won. Based on the conditions -
    Rock > Scissors
    Paper > Rock
    Scissors > Paper

    '''

    if (player == 'r' and opponent == 's') or \
        (player == 'p' and opponent == 'r')\
            or (player == 's' and opponent == 'p'):
        return True


if __name__ == '__main__':

    '''

    Constructor; Calls the play function to initiate the game

    '''
    result = play()
    print(result)

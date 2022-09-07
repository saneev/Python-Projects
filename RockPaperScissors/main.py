import random


def play():
    user = str(input("Enter 'r' for rock, 'p' paper, 's' for scissors:\t"))
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a Tie! Try again."
    elif IsWin(user, computer):
        return "You win! Congrats."

    return "You Lost! Try again"


def IsWin(player, opponent):

    if (player == 'r' and opponent == 's') or \
        (player == 'p' and opponent == 'r')\
            or (player == 's' and opponent == 'p'):
        return True


if __name__ == '__main__':
    print(play())

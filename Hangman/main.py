import random
import string
from words import words


def getValidWord(words):

    """

    Returns a valid word from the list of English Words

    """

    word = str(random.choice(words)).upper()

    while "-" in word or ' ' in word:
        word = str(random.choice(words))

    return word


def hangman():

    word = getValidWord(words)
    print(word)
    word_letters = set(word)  # Letters in the selected Word
    validAlphabets = set(string.ascii_uppercase)
    used_letters = set()  # Already used by the User
    lives = 3

    while len(word_letters) > 0 and lives > 0:

        print(f"You have {lives} lives remaining\n")

        print("Letters used:" + " ".join(used_letters))
        print("\n")

        word_list = []

        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')

        print("Current Word:", " ".join(word_list))
        print("\n")

        userInput = str(input("Please guess a letter: ")).upper()

        if userInput in validAlphabets - used_letters:
            used_letters.add(userInput)
            if userInput in word_letters:
                word_letters.remove(userInput)
            else:
                lives = lives - 1
        elif userInput in used_letters:
            print(
                "You have already used that letter.\
                Please try a different guess!\n"
            )
        else:
            print("\n")
            print("Invalid guess. Please try again!\n")

    if lives == 0:
        print(f'You lost!, You have {lives} lives, the word is {word}\n')
    else:
        print(f'You guess the word {word} right. Congrats!\n')


if __name__ == "__main__":

    hangman()

import random

def guess(limit):
    '''Method generates a random number that needs to be guessed by the player'''

    random_number = random.randint(1,limit)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Please guess a number between 1 and {limit}:\n'))
        if guess < random_number:
            print("Oops! The guess is too low. Please try again!")
        elif guess > random_number:
            print("Oops! The guess is too high. Please try again!")
    if guess == random_number:
        print(f"Yay! You guessed right. You guessed the number {random_number}")
        print("Thank you for playing with our bot")

if __name__ == '__main__':
    guess(10) #Calling the guess method to start the game
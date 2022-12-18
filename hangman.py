from random import *


def get_word():
    file = open('words.txt', 'r')
    line = file.readline()
    words = line.lower().split()
    secret_word = ''.join(sample(words, k=6))
    file.close()
    return secret_word


def word_guessed(secret_word):
    guess = input("Enter a word: ")
    guess = guess.lower()

    if guess in secret_word:
        return True, guess
    else:
        return False, guess


def print_guessed(secret_word, letters_guessed):
    mistakes_num = 0

    for letter in secret_word:
        if letter in letters_guessed:
            print(f"{letter}", end="")
        else:
            print("-", end="")
            mistakes_num += 1

    if mistakes_num == 0:
        print("\n")
        print(f"The secret word is {secret_word}, You won!")
        return True


def play_hangman():
    print("Hi, Welcome to Hangman Game\n")
    print("[1]: Easy, [2]: Medium, [3]: Hard")
    selection = int(input("Select level that you want to play (1~3) : "))

    if (selection == 1):
        # Easy mode
        MAX_GUESSES = 12
        print("You selected [easy] mode!")
    elif (selection == 2):
        # Medium mode
        MAX_GUESSES = 6
        print("You selected [medium] mode!")
    elif (selection == 3):
        # Hard mode
        MAX_GUESSES = 5
        print("You selected [hard] mode!")
    else:
        print("Please enter a correct selection.")
    print("\n Let's getting start!")

    secret_word = get_word()

    # secret_word = 'claptrap'
    letters_guessed = []

    while MAX_GUESSES > 0:
        (boolean, guess) = word_guessed(secret_word)

        if boolean == True:
            print("Correct!")
        else:
            MAX_GUESSES -= 1
            print("Incorrect!")
            print(MAX_GUESSES)

        letters_guessed.append(guess)
        breakpoint = print_guessed(secret_word, letters_guessed)

        if breakpoint == True:
            print(f"Your score is {MAX_GUESSES}")
            break


play_hangman()

# bootleg wordle

import random
from termcolor import colored


def compare_words(guess, word):
    for x in range(len(guess)):
        if guess[x] == word[x]:
            print(colored(guess[x], 'green'), end="")
        else:
            isThere = False
            for i in range(len(guess)):
                if guess[x] == word[i]:
                    if (word[i] == word[x]):
                        pass
                    else:
                        print(colored(guess[x], 'yellow'), end="")
                        isThere = True
                        break
            if not isThere:
                print("_", end="")
    print()


if __name__ == '__main__':
    word = random.choice(open("5letter_words.txt").read().split())
    print(word)
    number_of_tries = 5
    guess = input()[:5]
    while guess != word and number_of_tries != 0:
        compare_words(guess, word)
        guess = input()[:5]
        number_of_tries -= 1
    if number_of_tries > 0:
        print("You've guessed correctly!")
    else:
        print("you've ran out of tries")

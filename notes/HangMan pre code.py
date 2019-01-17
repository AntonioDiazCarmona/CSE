import random
import string
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle",]
the_word = random.choice(words)
print(the_word)
letters = list(string.ascii_letters)
turns_left = 10
failed = 0
letters_used = []

while turns_left > 0:
    # Create the output


    # Taking a guess
    letter = input("")
    letters_used.append(letter)
    if letter in the_word:
        print("I found one!")
        print(letters_used)
        print(letter)
    else:
        turns_left -= 1
        print("Wrong")
        print("You have", + turns_left, 'more guesses')
        print(letters_used)
        print(letter)
    if turns_left == 0:
        print("You Loose better luck next time")

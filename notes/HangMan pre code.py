name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("Start guessing...")
import random
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle",]
the_word = random.choice(words)
print(the_word)
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p""q","r","s","t","u","v","w","x","y","z"]
letter = input("")
if letter in the_word:
    print(letter)

turns_left = 10
turns = 10
while turns > 0:
    failed = 0
    letter = input("")
    if letter in the_word:
        print(letter)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Won")
guess = input("guess a letter")
turns_left += guess
if guess not in the_word:
    turns -= 1
    print("Wrong")
    print("You have", + turns, 'more guesses')
if turns == 0:
    print("You Loose")

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("Start guessing...")
import random
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle",]
the_word = random.choice(words)
string1 = (the_word)
list1 = list(string1)
print(list1)

print(the_word)
guesses = 10
turns = 10
while turns > 0:
    failed = 0
    for letter in the_word:
        if letter in guesses:
            print(letter)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Won")
guess = input("guess a letter")
guesses += guess
if guess not in the_word:
    turns -= 1
    print("Wrong")
    print("You have", + turns, 'more guesses')
if turns == 0:
    print("You Loose")
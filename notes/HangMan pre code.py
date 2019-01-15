import random
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle",]
the_word = random.choice(words)
print(the_word)
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p""q","r","s","t","u","v","w","x","y","z"]
turns_left = 10
failed = 0

while turns_left > 0:
    # Create the output

    # Taking a guess
    letter = input("")
    if letter in the_word:
        print("I found one!")
    else:
        turns_left -= 1
        print("Wrong")
        print("You have", + turns_left, 'more guesses')
    if turns_left == 0:
        print("You Loose better luck next time")

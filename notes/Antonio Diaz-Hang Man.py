import random
import string
words =["tomatoes","foodmax","fortnite","chicken","elephant","noodle","pepperoni","computer","pycharm","triangle","phone","spongebob","clifford"
        "star","book","exit","video","test","math","english","biology","dog","cat","alien","meteor","sentence","tissue","thanos","watermelon"]
the_word = random.choice(words)
# the_word = "CAPITAL LETTERS!!!"
# print(the_word)
letters = list(string.ascii_letters)
turns_left = 10
failed = 0
letters_used = []
hidden_word = []
list_of_letters_in_word = list(the_word)
# print(list_of_letters_in_word)

for character in list_of_letters_in_word:
    if character in letters:
        # replace with a *
        hidden_word.append("*")
    else:
        hidden_word.append(character)

while turns_left > 0:
    # Create the output
    print("".join(hidden_word))

    # Taking a guess
    letter = input("").lower()
    letters_used.append(letter)

    if letter in the_word.lower():
        print("I found one!")
        for i in range(len(the_word)):
            if the_word[i].lower() == letter:
                hidden_word.pop(i)
                hidden_word.insert(i, the_word[i])

    else:
        turns_left -= 1
        print("Wrong")
        print("You have", + turns_left, 'more guesses')
    print(letters_used)
    print(letter)
    if turns_left == 0:
        print("You Loose better luck next time")
    if "*" not in hidden_word:
            print("YOU WON")
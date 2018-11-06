import random

correct_number = random.randint(1,10)

guesses_remaining = 5

keep_playing = "true"
while keep_playing == "true":
    guess = int(input("Guess a number from 1-10........"))
    guesses_remaining = guesses_remaining - 1
    if guess == correct_number:
        print ("Correct you guess the number!")
        keep_playing = "false"
    else:
        if correct_number > guess:
            print ("To low")
        elif correct_number < guess:
            print ("To high")
    if guesses_remaining == 0:
        print ("Ran out of guesses. The correct guess was",correct_number)
        keep_playing = "false"

import random
a = random.randint(1, 10)
correct_number = random.randint(1, 10)
guesses_remaining = 5
guess = int(input("Enter number from 1 to 10: "))
while a !="guess":
    print
    if guess == correct_number:
        if guess < a:
            print("to low")
        guess = int(input("Enter number from 1 to 10: "))

        guesses_remaining = guesses_remaining - 1
    elif guess > a:
        print("to high")
        guess = int(input("Enter number from 1 to 10: "))
    else:
        print(" correct you guessed it!")
        if guesses_remaining == 0:
            print("Ran out of guesses")
    keep_playing = "false"
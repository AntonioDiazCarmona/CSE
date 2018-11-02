import random
a = random.randint(1, 10)
guess = int(input("Enter number from 1 to 10: "))
while a != "guess":
    print
    if guess < a:
        print("to low")
        guess = int(input("Enter number from 1 to 10: "))
    elif guess > a:
        print("to high")
        guess = int(input("Enter number from 1 to 10: "))
    else:
        print(" correct you guessed it!")
    break
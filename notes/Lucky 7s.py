import random

Money_remaining = 15
playing = True
while playing:
    First_Dice = random.randint(1, 6)
    Second_Dice = random.randint(1, 6)
    Add_dices == First_Dice += second_Dice:
    print("Your money for this round is",Money_remaining)


        if Money_remaining > guess:
            print("To low")
        elif Money_remaining < guess:
            print("To high")
if Money_remaining == 0:
    print("Ran out of money.Better luck next time")
    playing = False

import random
Dice_1 = random.randint(1, 6)
Dice_2 = random.randint(1, 6)
playing = True
Money = 15

while Money == 15:
    Money -= 1
    print(Dice_1 + Dice_2)
    if Dice_1 + Dice_2 == 7:
        print("you win,you now have ",15+4,"dollars now.")
        elif Dice_1 + Dice_2>7
        print("you lost.You now have",Money,"dollars now")
        elif Dice_1 + Dice_2<7
        print("you lost.you now have",Money,"dollars now")
    if Money == 0:
    print("Ran out of money.Better luck next time")
    playing = False




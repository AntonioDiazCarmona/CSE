import random
Dice_1 = random.randint(1, 6)
Dice_2 = random.randint(1, 6)
Money = 15
Round = 1
playing = True
while playing is True:
    while Money == 15:
        Money -= 1
    print(Dice_1 + Dice_2)
    if Dice_1 + Dice_2 == 7:
        print("you win,you now have ",Money+4,"dollars now.")
        if Dice_1 + Dice_2>7:
            print("you lost.You now have",Money,"dollars now")
        elif Dice_1 + Dice_2<7:
            print("you lost.you now have",Money,"dollars now")
            Round += 1
    if Money == 0:
        print("Ran out of money.Better luck next time")
    playing = False
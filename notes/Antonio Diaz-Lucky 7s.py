import random
roll_again = "yes"
money = 15
rounds = 0
while money > 0:
    print("rolling dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("The two values combined are...")
    print(dice1 + dice2)
    rounds += 1
    money -= 1
    myrole = (dice1 + dice2)
    if myrole == 7:
        money += 5
        print("your roll was a 7 you earned four dollars")
    elif myrole != 0:
        print("sorry you did not roll a 7,roll again?")
    elif money != 0:
        print("sorry you ran out of money")
print("sorry you loose. you played %d rounds" % rounds)

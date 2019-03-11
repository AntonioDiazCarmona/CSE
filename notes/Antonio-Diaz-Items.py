import random

class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Axe(Item):

    def __init__(self, name, weight, blade, damage, durability):
        super(Axe, self).__init__(name, weight)

        self.handle = True

        self.blade = blade

        self.damage = damage

        self.durability = durability

    def blade(self, long):
        self.blade = long

    def damage(self):
        self.damage = 10


class LongAxe(Axe):

    def __init__(self, name, damage, blade, durability, weight):

        super(LongAxe, self).__init__(name, weight, blade, damage, durability)

    def attack(self):

        if self.durability > 0:
            print("you did a heavy swing and did", self.damage, "damage")

            self.durability = self.durability - 5

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your long axe")

        else:

            print("you died")


Long_Axe = LongAxe("LongAxe", 30, "Long", 100, 20)

Long_Axe.attack()

Long_Axe.Amount_of_Durability()


class ShortAxe(Axe):

    def __init__(self, name, damage, blade, durability, weight):

        super(ShortAxe, self).__init__(name, weight, blade, damage, durability)

    def attack(self):

        if self.durability > 0:
            print("you did swing and did", self.damage, "damage")

            self.durability = self.durability - 5

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your short axe")

        else:

            print("you died")


Short_Axe = ShortAxe("ShortAxe", 15, "small", 50, 10)

Short_Axe.attack()

Short_Axe.Amount_of_Durability()


class Sword(Item):

    def __init__(self, name, weight, blade, damage, durability):
        super(Sword, self).__init__(name, weight)

        self.handle = True

        self.blade = blade

        self.damage = damage

        self.durability = durability

    def blade(self, long):
        self.blade = long

    def damage(self):
        self.damage = 10


class ShortSword(Sword):

    def __init__(self, name, damage, blade, durability, weight):

        super(ShortSword, self).__init__(name, weight, blade, damage, durability)

    def attack(self):

        if self.durability > 0:
            print("you did swing your short sword and did", self.damage, "damage")

            self.durability = self.durability - 5

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your short sword")

        else:

            print("you died")


Short_Sword = ShortSword("ShortSword", 5, "small", 50, 5)

Short_Sword.attack()

Short_Sword.Amount_of_Durability()


class LongSword(Sword):

    def __init__(self, name, damage, blade, durability, weight):

        super(LongSword, self).__init__(name, weight, blade, damage, durability)

    def attack(self):

        if self.durability > 0:
            print("you did swing your long sword and did", self.damage, "damage")

            self.durability = self.durability - 5

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your long sword")

        else:

            print("you died")


Long_Sword = LongSword("ShortSword", 5, "small", 50, 5)

Long_Sword.attack()

Long_Sword.Amount_of_Durability()


class Bow(Item):

    def __init__(self, name, weight, arrows, damage, durability):
        super(Bow, self).__init__(name, weight)

        self.arrows = arrows

        self.damage = damage

        self.durability = durability

    def arrows(self, long):
        self.arrows = long

    def damage(self):
        self.damage = 10


class LongBow(Bow):

    def __init__(self, name, weight, arrows, damage, durability):

        super(LongBow, self).__init__(name, weight, arrows, damage, durability)

    def shoot(self):

        if self.arrows > 0:

            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')

            self.arrows = self.arrows - 1

            self.durability = self.durability - 1

        else:

            print('...')

    def howManyArrowsLeft(self):

        if self.arrows > 0:

            print("You STILL have", self.arrows, "arrows left")

        else:

            print("You got nothing")

            print(self.arrows)

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your long bow")

        else:

            print("you have no durability")


Long_Bow = LongBow("Long Bow", 15, 10, 50, 500)

Long_Bow.shoot()

Long_Bow.howManyArrowsLeft()

Long_Bow.Amount_of_Durability()


class ShortBow(Bow):

    def __init__(self, name, weight, arrows, damage, durability):

        super(ShortBow, self).__init__(name, weight, arrows, damage, durability)

    def shoot(self):

        if self.arrows > 0:

            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')

            self.arrows = self.arrows - 1

            self.durability = self.durability - 1



        else:

            print('...')

    def howManyArrowsLeft(self):

        if self.arrows > 0:

            print("You STILL have", self.arrows, "arrows left")

        else:

            print("You got nothing")

            print(self.arrows)

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your long bow")

        else:

            print("you have no durability")


Short_Bow = ShortBow("Long Bow", 10, 30, 30, 300)

Short_Bow.shoot()

Short_Bow.howManyArrowsLeft()

Short_Bow.Amount_of_Durability()


class CrossBow(Bow):

    def __init__(self, name, weight, arrows, damage, durability):

        super().__init__(name, weight, arrows, damage, durability)

    def shoot(self):

        if self.arrows > 0:

            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')

            less_arrows = int(input("how many arows would you like to shoot? "))

            self.arrows = self.arrows - less_arrows

            self.durability = self.durability - less_arrows



        else:

            print('...')

    def howManyArrowsLeft(self):

        if self.arrows > 0:

            print("You STILL have", self.arrows, "arrows left")

        else:

            print("You got nothing")

            print(self.arrows)

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your long bow")

        else:

            print("you have no durability")


Cross_Bow = CrossBow("Long Bow", 10, 30, 30, 1000)

Cross_Bow.shoot()

Cross_Bow.howManyArrowsLeft()

Cross_Bow.Amount_of_Durability()


class Staff(Item):

    def __init__(self, name, weight, crystal, MagicDamage, durability):
        super(Staff, self).__init__(name, weight)

        self.handle = True

        self.crystal = crystal

        self.MagicDamage = MagicDamage

        self.durability = durability

    def crystal(self, long):
        self.Crystal = long

    def MagicDamage(self):
        self.MagicDamage = 10


class FireStaff(Staff):

    def __init__(self, name, weight, crystal, MagicDamage, durability):

        super(FireStaff, self).__init__(name, weight, crystal, MagicDamage, durability)

    def ShootFireBall(self):

        if self.durability > 0:

            print("you shot a fire ball and did ", self.MagicDamage,
                  "damage, The thing is also taking burn damage of 1 health per sec for 5 secs")

            self.durability = self.durability - 2

            # syncronous

            import time

            number_of_seconds = 5

            for _ in range(number_of_seconds):
                time.sleep(1)
                print("You are taking 1 damage do to fire damage from the fire ball")
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Fire Staff")
        else:
            print("you died")
Fire_Staff = FireStaff("FireStaff", 20, "Long", 60, 20)
Fire_Staff.ShootFireBall()
Fire_Staff.Amount_of_Durability()


class IceStaff(Staff):
    def __init__(self, name, weight, crystal, MagicDamage, durability):
        super(IceStaff, self).__init__(name, weight, crystal, MagicDamage, durability)
    def Freeze(self):
        if self.durability > 0:
            print("you shot a Ice ball and ", self.MagicDamage, "damage,You also froze the thing for 10 seconds")
            self.durability = self.durability - 2
            import time
            number_of_seconds = 10
            for _ in range(number_of_seconds):
                time.sleep(1)
                print("You are frozen ")
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Ice Staff ")
        else:
            print("you died")
Ice_staff = IceStaff("IceStaff", 20, "Long", 50, 35)
Ice_staff.Freeze()
Ice_staff.Amount_of_Durability()

#
# class  Shield(Item):
#     def __init__(self,name, weight, blockDamage, durability):
#         super(Shield, self).__init__(name, weight)
#         self.blockDamage = blockDamage
#         self.durability = durability
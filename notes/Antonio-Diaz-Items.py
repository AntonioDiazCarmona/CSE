import random

debug = True
if debug:
    delay = 0.01
else:
    delay = 1


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
                time.sleep(1 * delay)
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
                time.sleep(1 * delay)
                print("You are frozen ")
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Ice Staff ")
        else:
            print("you died")
Ice_staff = IceStaff("IceStaff", 20, "Long", 50, 35)
Ice_staff.Freeze()
Ice_staff.Amount_of_Durability()


class LightingStaff(Staff):
    def __init__(self, name, weight, crystal, MagicDamage, durability):
        super(LightingStaff, self).__init__(name, weight, crystal, MagicDamage, durability)
    def attack(self):
        if self.durability > 0:
            print("You shot a lighting ball and did ", self.MagicDamage, "damage")
            self.durability = self.durability - 1
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your lighting Staff")
        else:
            print("you died")
lighting_staff = LightingStaff("lighting staff", 15, "long", 100, 25)
lighting_staff.attack()
lighting_staff.Amount_of_Durability()


class shield(Item):

    def __init__(self, name, weight, blockdamage, durability):
        super(shield, self).__init__(name, weight)

        self.blockdamage = blockdamage

        self.durability = durability

    def blockdamage(self):
        blockdamage = 50


class ArmShield(shield):

    def __init__(self, name, weight, blockdamage, durability):

        super(ArmShield, self).__init__(name, weight, blockdamage, durability)

    def Block(self):

        if self.durability > 0:
            damage = int(input("how much damage would you like to recieve? "))

            self.Shield_broke(damage)

            # self.blockdamage = self.blockdamage - damage

            self.durability = self.durability - damage

            print("you blocked", damage, "damage")

    def Amount_of_Durability(self):

        if self.durability > 0:

            print("you still have", self.durability, "durability left on your arm shield")

        else:

            print("you ran out of durability and your shield broke")

    def Shield_broke(self, damage):

        if damage > self.blockdamage:
            print("Your shield broke by taking", self.blockdamage - damage,
                  "damage over the block damage of what "                                                              "the arm shield handle at a time")

            # else:

        #     print("you blocked", damage, "damage")


Arm_shield = ArmShield("Arm Shield", 10, 50, 1000)

Arm_shield.Block()

Arm_shield.Amount_of_Durability()

Arm_shield.Shield_broke(50)


class MythicalShield(shield):

    def __init__(self, name, weight, blockdamage, durability):

        super(MythicalShield, self).__init__(name, weight, blockdamage, durability)

    def Block(self):

        if self.durability > 0:
            damage = int(input("how much damage would you like to recieve on your mythical shield? "))

            self.durability = self.durability + damage  # changes

            print("You got attack and you mythical shield absorve", damage,
                  "damage and turned it into durabibility so your durability increase")

    def Amount_of_Durability(self):

        if self.durability > 0:
            print("you have ", self.durability, "durability after absorbing the damage you took  ")


Mythical_Shield = MythicalShield("Mythical Shield", 10, 0, 500)

Mythical_Shield.Block()

Mythical_Shield.Amount_of_Durability()


class NerfGun(Item):
    def __init__(self, name, weight, bullets, damage, durability):
        super(NerfGun, self).__init__(name, weight)
        self.bullets = bullets
        self.damage = damage
        self.durability = durability
    def bullets(self):
        self.bullets = bullets

    def damage(self):
        self.damage = damage

class AssaultRifle(NerfGun):
    def __init__(self, name, weight, bullets, damage, durability):
        super(AssaultRifle, self).__init__(name, weight, bullets, damage, durability)
    def shoot(self):
        if self.bullets > 0:
            print('You shot a nerf bullet  with your assault rifle and did ', self.damage, 'damage')
            self.bullets = self.bullets - 1
            self.durability = self.durability - 1
        else:
            print('...')
    def howManyBulletsLeft(self):
        if self.bullets > 0:
            print("You STILL have", self.bullets, "bullets left")
        else:
            print("You got nothing")
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your nerf assault rifle")
        else:
            print("you have no durability")
Assault_Rifle = AssaultRifle("Assault Rifle", 15, 30, 20, 200)
Assault_Rifle.shoot()
Assault_Rifle.howManyBulletsLeft()
Assault_Rifle.Amount_of_Durability()

class BurstRifle(NerfGun):
    def __init__(self, name, weight, bullets, damage, durability):
        super(BurstRifle, self).__init__(name, weight, bullets, damage, durability)
    def shoot(self):
        if self.bullets > 0:
            print('You shot 3 nerf bullets with your burst rifle and did ', self.damage, 'damage')
            self.bullets = self.bullets - 3
            self.durability = self.durability - 1
        else:
            print('...')
    def howManyBulletsLeft(self):
        if self.bullets > 0:
            print("You STILL have", self.bullets, "bullets left")
        else:
            print("You got nothing")
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your nerf burst rifle")
        else:
            print("you have no durability")
Burst_Rifle = BurstRifle("Burst Rifle", 15, 20, 15, 100)
Burst_Rifle.shoot()
Burst_Rifle.howManyBulletsLeft()
Burst_Rifle.Amount_of_Durability()








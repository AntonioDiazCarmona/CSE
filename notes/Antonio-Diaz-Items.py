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

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long axe")
        else:
            print("you died")


class ShortAxe(Axe):
    def __init__(self, name, damage, blade, durability, weight):
        super(ShortAxe, self).__init__(name, weight, blade, damage, durability)

    def attack(self):
        if self.durability > 0:
            print("you did swing and did", self.damage, "damage")
            self.durability = self.durability - 5

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your short axe")
        else:
            print("you died")


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

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your short sword")
        else:
            print("you died")


class LongSword(Sword):
    def __init__(self, name, damage, blade, durability, weight):
        super(LongSword, self).__init__(name, weight, blade, damage, durability)

    def attack(self):
        if self.durability > 0:
            print("you did swing your long sword and did", self.damage, "damage")
            self.durability = self.durability - 5

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long sword")
        else:
            print("you died")


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

    def how_many_arrows_left(self):
        if self.arrows > 0:
            print("You STILL have", self.arrows, "arrows left")
        else:
            print("You got nothing")
            print(self.arrows)

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long bow")
        else:
            print("you have no durability")


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

    def how_many_arrows_left(self):
        if self.arrows > 0:
            print("You STILL have", self.arrows, "arrows left")
        else:
            print("You got nothing")
            print(self.arrows)

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long bow")
        else:
            print("you have no durability")


class CrossBow(Bow):
    def __init__(self, name, weight, arrows, damage, durability):
        super().__init__(name, weight, arrows, damage, durability)

    def shoot(self):
        if self.arrows > 0:
            print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')
            less_arrows = int(input("how many arrows would you like to shoot? "))
            self.arrows = self.arrows - less_arrows
            self.durability = self.durability - less_arrows
        else:
            print('...')

    def how_many_arrows_left(self):
        if self.arrows > 0:
            print("You STILL have", self.arrows, "arrows left")
        else:
            print("You got nothing")
            print(self.arrows)

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your long bow")
        else:
            print("you have no durability")


class Staff(Item):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(Staff, self).__init__(name, weight)
        self.handle = True
        self.crystal = crystal
        self.MagicDamage = magic_damage
        self.durability = durability


class FireStaff(Staff):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(FireStaff, self).__init__(name, weight, crystal, magic_damage, durability)

    def shoot_fire_ball(self):
        if self.durability > 0:
            print("you shot a fire ball and did ", self.MagicDamage,
                  "damage, The thing is also taking burn damage of 1 health per sec for 5 secs")
            self.durability = self.durability - 2
            import time
            number_of_seconds = 5
            for _ in range(number_of_seconds):
                time.sleep(1 * delay)
                print("You are taking 1 damage do to fire damage from the fire ball")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Fire Staff")
        else:
            print("you died")


class IceStaff(Staff):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(IceStaff, self).__init__(name, weight, crystal, magic_damage, durability)

    def freeze(self):
        if self.durability > 0:
            print("you shot a Ice ball and ", self.MagicDamage, "damage,You also froze the thing for 10 seconds")
            self.durability = self.durability - 2
            import time
            number_of_seconds = 10
            for _ in range(number_of_seconds):
                time.sleep(1 * delay)
                print("You are frozen ")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your Ice Staff ")
        else:
            print("you died")


class LightingStaff(Staff):
    def __init__(self, name, weight, crystal, magic_damage, durability):
        super(LightingStaff, self).__init__(name, weight, crystal, magic_damage, durability)

    def attack(self):
        if self.durability > 0:
            print("You shot a lighting ball and did ", self.MagicDamage, "damage")
            self.durability = self.durability - 1

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your lighting Staff")
        else:
            print("you died")


class Shield(Item):
    def __init__(self, name, weight, blockdamage, durability):
        super(Shield, self).__init__(name, weight)
        self.blockdamage = blockdamage
        self.durability = durability


class ArmShield(Shield):
    def __init__(self, name, weight, blockdamage, durability):
        super(ArmShield, self).__init__(name, weight, blockdamage, durability)

    def block(self):
        if self.durability > 0:
            damage = int(input("how much damage would you like to recieve? "))
            self.shield_broke(damage)
            self.durability = self.durability - damage
            print("you blocked", damage, "damage")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your arm shield")
        else:
            print("you ran out of durability and your shield broke")

    def shield_broke(self, damage):
        if damage > self.blockdamage:
            print("Your shield broke by taking", self.blockdamage - damage,
                  "damage over the block damage of what the arm shield handle at a time")


class MythicalShield(Shield):
    def __init__(self, name, weight, blockdamage, durability):
        super(MythicalShield, self).__init__(name, weight, blockdamage, durability)

    def block(self):
        if self.durability > 0:
            damage = int(input("how much damage would you like to recieve on your mythical shield? "))
            self.durability = self.durability + damage  # changes
            print("You got attack and you mythical shield absorve", damage,
                  "damage and turned it into durabibility so your durability increase")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you have ", self.durability, "durability after absorbing the damage you took  ")


class NerfGun(Item):
    def __init__(self, name, weight, bullets, damage, durability):
        super(NerfGun, self).__init__(name, weight)
        self.bullets = bullets
        self.damage = damage
        self.durability = durability


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

    def how_many_bullets_left(self):
        if self.bullets > 0:
            print("You STILL have", self.bullets, "bullets left")
        else:
            print("You got nothing")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your nerf assault rifle")
        else:
            print("you have no durability")


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

    def how_many_bullets_left(self):
        if self.bullets > 0:
            print("You STILL have", self.bullets, "bullets left")
        else:
            print("You got nothing")

    def amount_of_durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left on your nerf burst rifle")
        else:
            print("you have no durability")


class ThrowingThings(Item):
    def __init__(self, name, weight, damage):
        super(ThrowingThings, self).__init__(name, weight)
        self.damage = damage


class Rock(ThrowingThings):
    def __init__(self, name, weight, damage):
        super(Rock, self).__init__(name, weight, damage)

    def throw(self):
        if self.damage > 0:
            print("you threw a rock and did", self.damage, "damage")
        else:
            print("You have no muscle and didn't throw the rock.")


class NinjaStar(ThrowingThings):
    def __init__(self, name, weight, damage):
        super(NinjaStar, self).__init__(name, weight, damage)

    def throw(self):
        if self.damage > 0:
            print("you threw a ninja star and did", self.damage, "damage")
        else:
            print("you threw the ninja star but missed...")


class ThingsInGame(Item):
    def __init__(self, name, weight, durability):
        super(ThingsInGame, self).__init__(name, weight)
        self.durability = durability


class Stool(ThingsInGame):
    def __init__(self, name, weight, durability):
        super(Stool, self).__init__(name, weight, durability)

    def place(self):
        if self.durability > 0:
            print("You placed the the stool and you can now reach the top of the statue with no head")
        else:
            print("you need to place the stool closer")


class Keys(ThingsInGame):
    def __init__(self, name, weight, durability):
        super(Keys, self).__init__(name, weight, durability)

    def rotate(self):
        if self.durability > 0:
            print("You rotates the key and opened the door")
        else:
            print("you need to rotate the key to open the mansion door")


# Instantiate Items
Long_Axe = LongAxe("LongAxe", 30, "Long", 100, 20)
Short_Axe = ShortAxe("ShortAxe", 15, "small", 50, 10)
Short_Sword = ShortSword("ShortSword", 5, "small", 50, 5)
Long_Sword = LongSword("ShortSword", 5, "small", 50, 5)
Long_Bow = LongBow("Long Bow", 15, 10, 50, 500)
Short_Bow = ShortBow("Long Bow", 10, 30, 30, 300)
Cross_Bow = CrossBow("Long Bow", 10, 30, 30, 1000)
Fire_Staff = FireStaff("FireStaff", 20, "Long", 60, 20)
Ice_staff = IceStaff("IceStaff", 20, "Long", 50, 35)
lighting_staff = LightingStaff("lighting staff", 15, "long", 100, 25)
Arm_shield = ArmShield("Arm Shield", 10, 50, 1000)
Mythical_Shield = MythicalShield("Mythical Shield", 10, 0, 500)
Assault_Rifle = AssaultRifle("Assault Rifle", 15, 30, 20, 200)
Burst_Rifle = BurstRifle("Burst Rifle", 15, 20, 15, 100)
rock = Rock("Rock", 4, 10)
Ninja_Star = NinjaStar("Ninja Star", 2, 15)
stool = Stool("stool", 10, 100)
key = Keys("Key", 1, 1000)

#  call what to do
Long_Axe.attack()
Long_Axe.amount_of_durability()
Short_Axe.attack()
Short_Axe.amount_of_durability()
Short_Sword.attack()
Short_Sword.amount_of_durability()
Long_Sword.attack()
Long_Sword.amount_of_durability()
Long_Bow.shoot()
Long_Bow.how_many_arrows_left()
Long_Bow.amount_of_durability()
Short_Bow.shoot()
Short_Bow.how_many_arrows_left()
Short_Bow.amount_of_durability()
Cross_Bow.shoot()
Cross_Bow.how_many_arrows_left()
Cross_Bow.amount_of_durability()
Fire_Staff.shoot_fire_ball()
Fire_Staff.amount_of_durability()
Ice_staff.freeze()
Ice_staff.amount_of_durability()
lighting_staff.attack()
lighting_staff.amount_of_durability()
Arm_shield.block()
Arm_shield.amount_of_durability()
Arm_shield.shield_broke(50)
Mythical_Shield.block()
Mythical_Shield.amount_of_durability()
Assault_Rifle.shoot()
Assault_Rifle.how_many_bullets_left()
Assault_Rifle.amount_of_durability()
Burst_Rifle.shoot()
Burst_Rifle.how_many_bullets_left()
Burst_Rifle.amount_of_durability()
Ninja_Star.throw()
rock.throw()
stool.place()
key.rotate()

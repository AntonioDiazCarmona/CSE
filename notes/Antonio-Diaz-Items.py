import random

class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Axe(Item):
    def __init__(self, name, weight, blade, damage):
        super(Axe, self).__init__(name, weight)
        self.handle = True
        self.blade = blade
        self.damage = damage

    def blade(self, long):
        self.blade = long

    def damage(self):
        self.damage = 10


class LongAxe(Axe):
    def __init__(self, name, damage, blade, durability, weight):
        super(Axe, self).__init__(name, weight, blade, damage,durability)
        self.name = name
        self.weight = weight
        self.damage = damage
        self.durability = 100
    def attack(self):
        if self.durability > 0:
            print("you did a heavy swing and did", self.damage, "damage")
            self.durability = self.durability - 10
    def Amount_of_Durability(self):
        if self.durability > 0:
            print("you still have", self.durability, "durability left")
        else:
            print("you died")

My_axe = Axe("LongAxe", 10, 100, )

My_axe.attack()

My_axe.Amount_of_health()

# class LongAxe(Axe):
#     def __init__(self, name, damage, health):
#         super(Axe, self).__init__(name, weight)
#         self.name = name
#         self.weight = weight
#         self.damage = damage
#         self.health = 100
#     def attack(self):
#         if self.health > 0:
#             print("you did a heavy swing and did", self.damage, "damage")
#             self.health = self.health - 10
#     def Amount_of_health(self):
#         if self.health > 0:
#             print("you still have", self.health, "health left")
#         else:
#             print("you died")
#
# Your_Axe = Axe("shortAxe", 10, 100)
#
# My_axe.attack()
#
# My_axe.Amount_of_health()





# class Sword(Item):
#     def __init__(self, name, weight, blade, damage):
#         super(Sword, self).__init__(name, weight)
#         self.handle = True
#         self.blade = blade
#         self.damage = damage
#
#     def blade(self, short):
#         self.blade = short
#
#     def damage(self):
#         self.damage = 10
#
#
# class ShortSword(Sword):
#     def __init__(self):
#         super(ShortSword, self).__init__("short sword", 15, "short", 15)
#
#     def attack(self):
#         return random.randint(12, 15)
#
#
# my_shortsword = ShortSword()
# print(my_shortsword.attack())
#
#
#      def __init__(self):
#          super(Crossbow, self).__init__("CrossBow", 20, 100, True, 30, 10)
#
#
# class Bow(Item):
#     def __init__(self, name, weight, arrows, damage):
#         super(Bow, self).__init__(name, weight)
#         self.name = name
#         self.weight = weight
#         self.arrows = arrows
#         self.damage = damage
#
#     def shoot(self):
#         if self.arrows > 0:
#             print('swishh swishh I just shot an arrow, you got hit and received', self.damage, 'damage')
#             self.arrows = self.arrows - 1
#         else:
#             print('...')
#     def howManyArrowsLeft(self):
#         if self.arrows > 0:
#             print("You STILL have", self.arrows, "left")
#         else:
#             print("You got nothing")
#             # always printing the number
#             print(self.arrows)
# class CrossBow(Bow):
#     def __init__(self):
#         super(CrossBow, self).__init__("MyFavBow", 15, 20, 15)
# myFavBow = CrossBow
# myFavBow.shoot()
#
# myFavBow.howManyArrowsLeft()
#

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

    def Axe(self, long):
        self.blade = long

    def damage(self):
        self.damage = 10


class LongAxe(Axe):
    def __init__(self, name, weight):
          super(LongAxe, self).__init__(name, weight, "long", 10)
my_axe = LongAxe

class Sword(Item):
    def __init__(self, name, weight, blade, damage):
        super(Sword, self).__init__(name, weight)
        self.handle = True
        self.blade = blade
        self.damage = damage

    def blade(self, short):
        self.blade = short

    def damage(self):
        self.damage = 10


class ShortSword(Sword):
    def __init__(self):
        super(ShortSword, self).__init__("short sword", 15, "short", 15)

    def attack(self):
        return random.randint(12, 15)


my_shortsword = ShortSword()
print(my_shortsword.attack())

class Bow(Item):
     def __init__(self, name, weight, range, shoot, damage, arrows = 10):
         super(Bow, self).__init__(name, weight)
         self.range = range
         self.shoot = shoot
         self.damage = damage
         self.arrows = arrows

     def damage(self):
          self.damage = 30

    def range(self):
        self.range = 100

    def shoot(self):
        self.shoot = True
    else:
        print("You have to press the trigger!")
    def arrows = 10
    if shoot(self= True -=1 arrows)
class Crossbow(Bow):
     def __init__(self):
         super(Crossbow, self).__init__("CrossBow", 20, 100, True, 30, 10)
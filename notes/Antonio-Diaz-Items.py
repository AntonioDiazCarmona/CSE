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


class Sword(Item):
    class ShortSword(Item):
        def __init__(self, name, weight, blade, damage):
            super(Sword, self).__init__(name, weight)
            self.handle = True
            self.blade = blade
            self.damage = damage

        def ShortSword(self, short):
            self.blade = short

        def damage(self):
            self.damage = 10

    class ShortSword(Sword):
        def __init__(self, name, weight):
            super(ShortSword, self).__init__(name, weight, "Short", 10)








    my_axe = LongAxe("Bertha", 15)
    My_sword = ShortSword("idk",5)
class Items(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Axe(Items):
    def __init__(self, name, types, blade, damage):
        super(Axe, self).__init__(name, types)
        self.handle = True
        self.blade = blade
        self.damage = damage


    def Axe(self, short):    # fix this
        self.blade = short

        def damage(self):
            self.damage = 10


  class LongAxe(Axe):
      def __init__(self):
          super(LongAxe,self).__init__(name, types)
          self.collectable
          my_Axe = LongAxe




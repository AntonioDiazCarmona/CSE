class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Things_you_can_pick_up(Item):
    def __init__(self, name, weight):

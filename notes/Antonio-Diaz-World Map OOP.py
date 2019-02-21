class Room(object):
    def __init__(self, name, description ="", north=None ,south=None, east=None,west = None, up = None, down = None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.west = west
        self.up = up
        self.down = down

ABANDONED_MANSION':{
        'NAME': "Abandoned  Mansion",
        'DESCRIPTION': "What your looking at is an abandoned mansion from the gate door a mile away"
                       "This mansion who no one know's who built it or who live here and some people have even said "
                       "that"
                       "The Mansion has been abandoned for centuries and it has stayed the same."
                       "The mansion has 15 rooms or does it? It also has a random statue with no head",
        'PATHS': {
            'SOUTH': "MANSION_DOOR"
        }





Abandoned_mansion = Room("Abandoned Mansion", "This mansion who no one know's who built it or who live here and some"
                                              " people have even said that the mansion has been abandoned for centuries"
                                              " and it has stayed the same. THe mansion has 15 rooms or does it?"
                                              " It also has a random statue with no head")

Mansion_door = Room("The ABANDONED MANSION DOOR", "The door seems to be closed and around you can see plants."
                                                " To the south there is a window.To the west is a statue that"
                                                " has no head.The door seems to be closed and around you can see"
                                                " plants.")

MANSION_WINDOW = Room("EAST SIDE WINDOW","The window seems to be a mirror ")

EAST_SIDE_OF_MANSION  =  Room("EAST SIDE OF MANSION","The east side of the mansion seems to be blocked off by a giant"
                                                     " tree." )






#option 1
# add the dependent rooms after
R19A = Room("R19A")
parking_lot = Room('The parking lot',None,R19A)
R19A.north = parking_lot
#option 2
#put them in quotes
R19A = Room("R19A", 'Parking_lot')
parking_lot = Room ("The parking lot",None,R19A)
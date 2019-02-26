class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.west = west
        self.up = up
        self.down = down


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """this method moves charecters to a new location

        :param newlocation:  the variable containing a room object
        """
        self.current_location = new_location






ABANDONED_MANSION = Room("Abandoned Mansion", "What your looking at is an abandoned mansion from the gate door a mile "
                                              "away"
                                              "This mansion who no one know's who built it or who live here and some"
                                              " people have even said that the mansion has been abandoned for centuries"
                                              " and it has stayed the same. THe mansion has 15 rooms or does it?"
                                              " It also has a random statue with no head")
player = Player(ABANDONED_MANSION)

MANSION_DOOR = Room("The ABANDONED MANSION DOOR", "The door seems to be closed and around you can see plants."
                                                  " To the south there is a window. To the west is a statue that"
                                                  " has no head.The door seems to be closed and around you can see"
                                                  " plants.")

MANSION_WINDOW = Room("EAST SIDE WINDOW", "The window seems to be a mirror ")

EAST_SIDE_OF_MANSION = Room("EAST SIDE OF MANSION", "The east side of the mansion seems to be blocked off by a giant"
                                                     "tree.")
V2MANSION_WINDOW = Room("WEST SIDE WINDOW OF MANSION", "You are back to the window that seems to be a mirror")

STATUE = Room("Cobblestone statue", "What your looking at is a coble stone statue of a man with no head "
                      "You can see a metal piece on top of the statue with there is no head"
                      "the statue is to high you will need something to climb on the statue and get the metal piece")

V1_SIDE_OF_MANSION = Room("south side of mansion", "You are looking at the south side of mansion which leads"
                                                  "to the backyard")

DOWN_SIDE_OF_MANSION = Room("Down south side of mansion", "You are walking down the south side of mansion")

BACKYARD_OF_MANSION = Room("EAST BACKYARD", "You are at the back yard and their seems to be alot of items at"
                                           " the backyard like stools,slide,and a small little tree")     # here you would get a stool

V2_SIDE_OF_MANSION = Room("WEST SIDE OF MANSION","You are looking at the side of the mansion you came from")

UP_SIDE_OF_MANSION = Room("UP NORTH,WEST SIDE OF MANSION","This is the way you came from in the begining to"
                                                          " go to the back yard")

V3_SIDE_OF_MANSION = Room("West side of mansion","You are at the west side of mansion to the east you"
                                                 " can see the coble stone statue from before")

COBBLE_STONE_STATUE = Room("WEST COBBLE STONE STATUE", "You are at the cobble stone statue now try to see what"
                                                       " is the top of the cobblestone statue with no head"
                                                       "by placing the stool that you collected from the"# you find the key...
                                                       " backyard and try climbing it to see what was"
                                                       " at the top of the no head statue")

V2MANSION_DOOR = Room("FRONT MANSION DOOR", "Your are back again to front mansion now try to open with"
                                            " the key you got from the "             
                                            "top of the cobbles stone statue with not head")  # you get the key

INSIDE_MANSION = Room("INSIDE OF MANSION", "Their seems to be a lot of rooms here.Their are two stair leading up to "
                                           "the second floor which where you can see more rooms.Their is also a"
                                           " random doll sitting on the stairs")
# you open the door with the key,get in.

ABANDONED_MANSION.south = MANSION_DOOR
MANSION_DOOR.east = MANSION_WINDOW
MANSION_WINDOW.east = EAST_SIDE_OF_MANSION
EAST_SIDE_OF_MANSION.west = V2MANSION_WINDOW
V2MANSION_WINDOW.west = MANSION_DOOR
MANSION_DOOR.West = STATUE               # here where you keep going
STATUE.south = V1_SIDE_OF_MANSION
V1_SIDE_OF_MANSION.south = DOWN_SIDE_OF_MANSION
DOWN_SIDE_OF_MANSION.east = BACKYARD_OF_MANSION
BACKYARD_OF_MANSION.west = V2_SIDE_OF_MANSION
V2_SIDE_OF_MANSION.north = UP_SIDE_OF_MANSION
UP_SIDE_OF_MANSION.east = V3_SIDE_OF_MANSION
V3_SIDE_OF_MANSION.east = COBBLE_STONE_STATUE
COBBLE_STONE_STATUE.east = V2MANSION_DOOR
V2MANSION_DOOR.south = INSIDE_MANSION
# #option 1
# # add the dependent rooms after
# R19A = Room("R19A")
# parking_lot = Room('The parking lot',None,R19A)
# R19A.north = parking_lot
# #option 2
# #put them in quotes
# R19A = Room("R19A", 'Parking_lot')
# parking_lot = Room ("The parking lot",None,R19A)
playing = True
directions = ["north", "south", "east", "west", "up", "down"]

# controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            #command ='north'       #if their is now location you put none                           # so this basically tell it if i has a path to north
            room_object_that_we_move_to = getattr(player.current_location,command)
            player.move(room_object_that_we_move_to)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")

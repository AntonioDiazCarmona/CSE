# world_map = {
#     'R19A': {
#         'NAME': "Wiebe's Classroom",
#         'DESCRIPTION': "This is the classroom that you are in right "
#                        "now. It has two exits to the north side.",
#         'PATHS': {
#             'NORTH': "PARKING_LOT"
#         }
#     },
#     'PARKING_LOT': {
#         'NAME': "The Edison Parking Lot",
#         'DESCRIPTION': "There are cars parked here. To "
#                        "the south is Mr. Wiebe's room",
#         'PATHS': {
#             'SOUTH': "R19A"
#         }
#     }
# }


world_map = {
    'ABANDONED_MANSION':{
        'NAME': "Abandoned  Mansion",
        'DESCRIPTION': "What your looking at is an abandoned mansion from the gate door a mile away"
                       "This mansion who no one know's who built it or who live here and some people have even said "
                       "that"
                       "The Mansion has been abandoned for centuries and it has stayed the same."
                       "The mansion has 15 rooms or does it? It also has a random statue with no head",
        'PATHS': {
            'SOUTH': "MANSION_DOOR"
        }
    },
    'MANSION_DOOR':{
        'NAME': "The ABANDONED MANSION DOOR",
        'DESCRIPTION': "The door seems to be closed and around you can see plants."
                       " To the south there is a window ."
                       "To the west is a statue that has no head.",
        'PATHS': {
            'EAST': "MANSION_WINDOW",
            'WEST': "STATUE"     # NEED TO ADD A NORTH TO GO BACK
        }
    },
    'MANSION_WINDOW': {
        'NAME': "EAST_SIDE_WINDOW",
        'DESCRIPTION': "The window seems to be a mirror ",
        'PATHS': {
            'WEST': "EAST SIDE OF MANSION"                                        # YOU CAN KEEP GOING HERE
        }
    },
    "EAST_SIDE_OF_MANSION": {
       'NAME': "EAST SIDE OF MANSION",
        'DESCRIPTION': "The east side of the mansion seems to be blocked off by a giant tree.",
        'PATHS': {
            'WEST':"V2MANSION WINDOW"
        }
    },
    "V2MANSION_WINDOW":{
        'NAME': "WEST SIDE WINDOW OF MANSION",
            'DESCRIPTION': " You are back to the window that seems to be a mirror",
            'PATHS': {
                'WEST':"MANSION DOOR"                     # I THINK IM FINISHED WITH THE EAST PATHWAY
        }
    },
    "STATUE": {
        'NAME': "Cobblestone statue ",
        'DESCRIPTION':"What your looking at is a coble stone statue of a man with no head "
                      "You can see a metal piece on top of the statue with there is no head"
                      "the statue is to high you will need something to climb on the statue and get the metal piece",
        'PATHS':{
            'SOUTH': "V1_SIDE OF MANSION"
        }
    },
    "V1_SIDE_OF_MANSION": {
            'NAME': "South side of mansion",
        "DESCRIPTION": "You are looking at the south side of mansion which leads to the backyard",
        'PATHS':{
            'SOUTH':"you are going down the side of mansion",
        }
    },
    "DOWN_SIDE_OF_MANSION": {
            'NAME': "Down south side of mansion",
        "DESCRIPTION": "You are walking down the south side of mansion",
        'PATHS':{
                'EAST':"You are at the backyard"
        }
    },
    "BACKYARD_OF_MANSION": {
            'NAME': "EAST BACKYARD",
        "DESCRIPTION": "You are at the back yard and their seems to be alot of items at the back like stools,slide,"
                       "and a small little tree",
        'PATHS':{      # HERE WE HAVE TO PUT WHERE WE PICK UP ITEMS
            'WEST':"Side of Mansion"
        }
    },
    "V2_SIDE_OF_MANSION": {
            'NAME':" WEST SIDE OF MANSION",
        "DESCRIPTION":" You are looking at the side of the mansion you came from",
        'PATHS':{
            'NORTH': "UP SIDE OF MANSION"
        }
    },
    "UP_SIDE_OF_MANSION": {
        'NAME': "UP NORTH,WEST SIDE OF MANSION",
        'DESCRIPTION': "This is the way you came from in the begining to go to the back yard",
        'PATHS': {
            'EAST':"SIDE OF MANSION"
        }
    },
    "V3_SIDE_OF_MANSION": {
        'NAME': "WEST SIDE OF MANSION",     # CONFUSED
        'DESCRIPTION': "You are at the west side of mansion to the east you can see the coble stone statue from before",
        'PATHS': {
            'EAST':"COBBLE STONE STATUE"
        }
    },
    "COBBLE_STONE_STATUE": {
        'NAME': "WEST COBBLE STONE STATUE",
        # where you place the stool to look on top of the statue with no head
        'DESCRIPTION': "You are at the cobble stone statue now try to see what is the top of the coblestone statue with no head"
                "by placing the stool in climbing it",    # this is where you would check and their is going to be a key to the mansion
        'PATHS': {
            'EAST':"V2MANSION_DOOR"
        }
    },

    "V2MANSION_DOOR":{
        'NAME': "FRONT MANSION DOOR",
        'DESCRIPTION': "Your are back againg to front mansion now try to open with the key you got from the "
                       "top of the cobbles stone statue with not head",
        'PATHS': {
            'SOUTH':"INSIDE_MANSION"
        }
    },
    "INSIDE MANSION": {
        'NAME': "INSIDE OF MANSION",
        'DESCRIPTION': "Their seems to be alot of rooms here.Their are two stair leading up to the second floor which"
                       "where you can see more rooms.Their is also a random doll sitting on the stairs",
        'PATHS': {
            '':""
        }
    }
}







#other variables
current_node = world_map['MANSION_DOOR']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True
# controller
while playing:
    print(current_node['NAME'])
    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    elif command.upper() in directions:
         try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = world_map[room_name]
         except KeyError:
             print("I can't go that way.")
    else:
         print("Command Not Recognized")
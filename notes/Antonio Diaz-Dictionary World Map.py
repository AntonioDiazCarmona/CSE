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
    'R19A':{
        'NAME': "Abandoned  Mansion",
        'DESCRIPTION': "What your looking at is an abandoned mansion from the gate door a mile away"
                       "This mansion who no one know's who built it or who live here and some people have even said that"
                       "The Mansion has been abandoned for centuries and it has stayed stay the same."
                       "The mansion has 9 rooms and 9 door or does it? it also has 9 statues which are flip upside down",
        'PATHS': {
            'SOUTH': "MANSION_DOOR"
        }
    },
    'MANSION_DOOR':{
        'NAME': "The ABANDONED MANSION DOOR",
        'DESCRIPTION':"There are plants here and "
        " to the south is a window where you can look through",
        'PATHS': {
            'EAST': "Mansion_Window",
            'WEST': "STATUE"
        }
    },
    "STATUE": {
        'NAME': "Cobblestone statue ",
        'DESCRIPTION':"What your looking at is a coble stone statue of a man with no head "
                      "You can see a metal piece on top of the statue with there is no head"
                      "the statue is to high you will need something to climb on the statue and get the metal piece",
        'PATHS':{
            'SOUTH': "SIDE OF MANSION"
        }
    },
    "SIDE OF MANSION": {
            'NAME': "South side of mansion",
        "DESCRIPTION": "You are walking throught the south side of mansion which leads to the backyard",
        'PATHS':{
            'DOWN':"you are going down the side of mansion",
           'EAST':"Back yard of mansion"
        }
    }
},



#other variables
current_node = world_map['MANSION_DOOR']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True
# controller
while playing:
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
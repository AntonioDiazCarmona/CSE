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
        'paths': {
            'EAST': "Mansion_Window",
            'WEST': "STATUE"
        }
    },
    "STATUE": {
        'NAME': "Coble stone statue "
        'DESCRIPTION':
    }
}
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
             print("command Not Recognized")
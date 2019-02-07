states = {
    "CA": "california",
    "VA": "virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}

print(states["CA"])
print(states["NV"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000 # 39,540,000
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION":8500000                    #8,500,000
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION":6000000                    #6,000,000
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315                   #1,057,315
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392                   #3,034,392
    }
}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000, # 39,540,000
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION":8500000,                    #8,500,000
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexandria"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000,                    #6,000,000
        "CITIES": [
            "Besthesda",
            "Baltimore",
            "Annnapolis"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,                  #1,057,315
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392,                   #3,034,392
        "CITIES": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}
print(complex_dictionary["RI"]["CITIES"][2])

print(complex_dictionary["VA"]["NAME"])
print(complex_dictionary["NV"]["CITIES"][0])

print(complex_dictionary.keys()) # get all  states
print(nested_dictionary.items())

print()
for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)
for state, facts in complex_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print ("-" * 20)

#other notes
states['AL'] = "Alaska?"    # it isnt alaska
# changing dictionart value
states['AL'] = "Alabama" # its actually alabama
## world_map = {
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


# world_map = {
#     'R19A':{
#         'NAME': "Abandoned  Mansion",
#         'DESCRIPTION': "What your looking at is an abandoned mansion from the gate door a mile away"
#                        "This mansion who no one know's who built it or who live here and some people have even said that"
#                        "The Mansion has been abandoned for centuries and it has stayed stay the same."
#                        "The mansion has 9 rooms and 9 door or does it? it also has 9 statues which are flip upside down",
#         'PATHS': {
#             'SOUTH': "MANSION_DOOR"
#         }
#     },
#     'MANSION_DOOR':{
#         'NAME': "The ABANDONED MANSION DOOR",
#         'DESCRIPTION':"The door seems to be closed and around are plants and "
#         " to the south is a window where you can look through",
#         'PATHS': {
#             'EAST': "MANSION_WINDOW",
#             'WEST': "STATUE"
#         }
#     },
#     'MANSION_WINDOW': {
#         'NAME': "EAST SIDE WINDOW",
#         'DESCRIPTION': "The window seems to be a mirror ",
#         'PATHS': {
#             'WEST': "STATUE"                                        # YOU CAN KEEP GOING HERE
#         }
#     },
#     "STATUE": {
#         'NAME': "Cobblestone statue ",
#         'DESCRIPTION':"What your looking at is a coble stone statue of a man with no head "
#                       "You can see a metal piece on top of the statue with there is no head"
#                       "the statue is to high you will need something to climb on the statue and get the metal piece",
#         'PATHS':{
#             'SOUTH': "SIDE OF MANSION"
#         }
#     },
#     "SIDE OF MANSION": {
#             'NAME': "South side of mansion",
#         "DESCRIPTION": "You are looking at the south side of mansion which leads to the backyard",
#         'PATHS':{
#             'SOUTH':"you are going down the side of mansion",
#         }
#     },
#     "DOWN SIDE OF MANSION": {
#             'NAME': "Down south side of mansion",
#         "DESCRIPTION": "You are walking down the south side of mansion",
#         'PATHS':{
#                 'EAST':"You are at the backyard"
#         }
#     },
#     "BACKYARD OF MANSION": {
#             'NAME': "EAST BACKYARD",
#         "DESCRIPTION": "You are at the back yard and their seems to be alot of items at the back like stools,slide,"
#                        "and a small little tree",
#         'PATHS':{      # HERE WE HAVE TO PUT WHERE WE PICK UP ITEMS
#             'WEST':"Side of Mansion"
#         }
#     },
#     "SIDE OF MANSION": {
#             'NAME':" WEST SIDE OF MANSION",
#         "DESCRIPTION":" You are looking at the side of the mansion you came from",
#         'PATHS':{
#             'NORTH': "UP SIDE OF MANSION"
#         }
#     },
#     "UP SIDE OF MANSION": {
#         'NAME': "UP NORTH SIDE OF MANSION",
#         'DESCRIPTION': "This is the way you came from in the begining to go to the back yard",
#         'PATHS': {
#             'EAST':"SIDE OF MANSION"
#         }
#     },
#     "SIDE OF MANSION": {
#         'NAME': "SIDE OF MANSION THAT lEAD TO THE SIDE OF MANSION",
#         'DESCRIPTION': "You are at the west side of mansion to the east you can see the coble stone statue from before",
#         'PATHS': {
#             'EAST':"COBBLE STONE STATUE"
#         }
#     },
#     "": {
#         'NAME': "",
#         # where you place the stool to look on top of the statue with no head
#         'DESCRIPTION': "",
#         'PATHS': {
#         }
#     }
# }
#
# #other variables
# current_node = world_map['MANSION_DOOR']
# directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
# playing = True
# # controller
# while playing:
#     command = input(">_")
#     if command.lower() in ('q', 'quit', 'exit'):
#         playing = False
#     elif command.upper() in directions:
#          try:
#             room_name = current_node["PATHS"][command.upper()]
#             current_node = world_map[room_name]
#          except KeyError:
#              print("I can't go that way.")
#          else:
#              print("Command Not Recognized")
'NAME': "",
'DESCRIPTION': "",
'PATHS': {
    '':
}
},

world_map = {
    'R19A':{
        'NAME': "Wiebe's classroom",
        'DESCRIPTION': "This is the classroom that you are in right now."
                       "It has two exits to the north side",
        'PATHS': {
        "NORTH": "PARKING_LOT"
        }
    }
    'PARKING_LOT':{
        'NAME' : "The Edison parking lot",
        'DESCRIPTION':"There are cars parked here.to"
        "the south is MR.Wiebe's room",
        'paths': {
            'SOUTH': "R19A"
        }
    }
}
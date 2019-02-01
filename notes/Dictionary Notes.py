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
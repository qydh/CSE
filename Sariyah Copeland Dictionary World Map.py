world_map = {
    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "You are in the kitchen. On the stove sits a pot and a pan",
        'PATHS': {
            'SOUTH': 'LIVING ROOM'
        }
    },
    'LIVING ROOM': {
        'NAME': 'Living Room',
        'DESCRIPTION': "You are in the living room connected to the kitchen",
        'PATHS': {
            'WEST': 'DINING ROOM',
            'EAST': 'BEDROOM 1'
        }
    },
    'DINING ROOM': {
        'NAME': 'Dining Room',
        'DESCRIPTION': "You are in the dining room connected to the kitchen",
        'PATHS': {
            'WEST': 'KITCHEN'
        }
    },
    'BEDROOM 1': {
        'NAME': "Bedroom 1",
        'DESCRIPTION': "You are in the aquarium themed bedroom",
        'PATHS': {
            'SOUTH': 'LIVING ROOM'
        }
    },
    'PANTRY': {
        'NAME': 'Pantry',
        'DESCRIPTION': "You are in the one entry way pantry",
        'PATHS': {
            'WEST': 'DINING ROOM'
        }
    },
    'GARAGE': {
        'NAME': 'Garage',
        'DESCRIPTION': "You are in the one entry way garage",
        'PATHS': {
            'WEST': 'NONE'
        }
    },
    'DEN': {
        'NAME': "Den",
        'DESCRIPTION': "You are in the small den with one entry way",
        'PATHS': {
            'SOUTH': 'LIVING ROOM'
        }
    },
    'SHOP': {
        'NAME': 'Shop',
        'DESCRIPTION': "You are in the one entry way small shop",
        'PATHS': {
            'WEST': 'BEDROOM 1'
        }
    },
    'BACKYARD': {
        'NAME': 'Backyard',
        'DESCRIPTION': "You are in the Backyard with 2 big dogs locked in a cage",
        'PATHS': {
            'WEST': 'DEN'
        }
    },
    'DECK': {
        'NAME': "Deck",
        'DESCRIPTION': "You are on the deck near the swimming pool",
        'PATHS': {
            'SOUTH': 'BACKYARD'
        }
    },
    'CLOSET 1': {
        'NAME': 'Closet 1 ',
        'DESCRIPTION': "You are in the first closet with one entry",
        'PATHS': {
            'WEST': 'CLOSET 2'
        }
    },
    'CLOSET 2': {
        'NAME': 'Closet 2 ',
        'DESCRIPTION': "You are in the second closet with one entry",
        'PATHS': {
            'WEST': 'BEDROOM 2'
        }
    },
    'MASTER BEDROOM': {
        'NAME': "Master Bedroom",
        'DESCRIPTION': "You are in the main bedroom with king and queen themed accessories",
        'PATHS': {
            'SOUTH': 'LIVING ROOM'
        }
    },
    'BEDROOM 2': {
        'NAME': 'Bedroom 2',
        'DESCRIPTION': "You are in the second bedroom that is sports themed",
        'PATHS': {
            'WEST': 'CLOSET 1'
        }
    },
    'BEDROOM 3': {
        'NAME': 'Bedroom 3',
        'DESCRIPTION': "You are in the last bedroom that has a princess theme",
        'PATHS': {
            'WEST': 'SHOP'
        }
    }
}

current_node = world_map['KITCHEN']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHWEST', 'SOUTHEAST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not recognized')
        print()
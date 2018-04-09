class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


room1 = Room("Kitchen", None, 'living', None, None,
             "You are in the kitchen. On the stove sits a pot and a pan")
living = Room("Living Room", 'room1', None, 'dining room', None,
              "You are in the living room connected to the kitchen")
dining = Room("Dining Room", 'dining room', 'kitchen', 'living room', 'pantry',
              "You are in the dining room connected to the kitchen")
bedroom1 = Room("Bedroom 1", 'kitchen', None, None, None,
                "You are in the aquarium themed bedroom")
pantry = Room("Pantry", 'kitchen', 'dining room', 'pantry', 'living room',
              "You are in the one entry way pantry")
garage = Room("Garage", 'den', 'shop', 'deck', 'backyard',
              "You are in the one entry way garage")
den = Room("Den", 'garage', 'shop', 'backyard', 'deck',
           "You are in the small den with one entry way")
shop = Room("Shop", 'den', 'garage', 'deck', 'backyard',
            "You are in the one entry way small shop")
backyard = Room("Backyard", 'deck', 'shop', 'den', 'garage',
            "You are in the Backyard with 2 big dogs locked in a cage")
deck = Room("Deck", 'backyard', 'den', 'closet 1', 'bedroom2',
            "You are on the deck near the swimming pool")
closet1 = Room("Closet 1", 'bedroom 2', 'closet 2', 'bedroom 3', 'master bedroom',
               "You are in the first closet with one entry")
closet2 = Room("Closet 2", 'bedroom 3', 'closet 1', 'master bedroom', 'bedroom 2',
               "You are in the second closet with one entry")
master_bedroom = Room("Master bedroom", 'closet 2', 'bedroom 3', 'bedroom 2', 'closet 1',
                      "You are in the main bedroom with king and queen themed accessories")
bedroom2 = Room("Bedroom 2", 'closet 1', 'bedroom 2', 'closet 2', 'master bedroom',
                "You are in the second bedroom that is sports themed")
bedroom3 = Room("Bedroom 3", 'master bedroom', 'closet2', 'bedroom 2', 'closet 1',
                "You are in the last bedroom that has a princess theme")

current_node = room1
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not recognized')
        print()
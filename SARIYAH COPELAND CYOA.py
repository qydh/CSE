class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Key(Item):
    def __init__(self):
            super(Key, self).__init__(
                "Key", "You have found the key that unlocks most of the rooms in the house"
            )


class Flashlight(Item):
    def __init__(self):
            super(Flashlight, self).__init__(
                "Flashlight", "You have found the flashlight. "
                              "You may need to find some batteries"
            )


class Batteries(Item):
    def __init__(self):
            super(Batteries, self).__init__("Batteries", "You have found 2 batteries.")


class Bag(Item):
    def __init__(self):
        super(Bag, self).__init__("Bag", "You have found a bag. "
                                         "You can use it to carry a few items."
                                  )


class Bone(Item):
    def __init__(self):
        super(Bone, self).__init__("Bone", "You have found a bone. "
                                           "You may need to use it to get passed the dogs."
                                   )


class Map(Item):
    def __init__(self):
        super(Map, self).__init__("Map", "You have found a map."
                                         " You can use it to make your way around the house."
                                  )


class Watch(Item):
    def __init__(self):
        super(Watch, self).__init__("Watch", "You have found a watch."
                                             "You can use it to keep track of time."
                                    )


class Computer(Item):
    def __init__(self):
        super(Computer, self).__init__("Computer", "On the desk there is a computer. "
                                       "But it doesnt work. It's there just to be there"
                                       )


class Bandages(Item):
    def __init__(self):
        super(Bandages, self).__init__("Bandages", "You can use these bandages and first aid kit to "
                                                   "treat care for yourself after you get injured")


class Helmet(Item):
    def __init__(self):
        super(Helmet, self).__init__("Helmet", "Wear this helmet so you wont take as "
                                               "much damage when fighting your enemy"
                                     )


class HealingPotion(Item):
    def __init__(self):
        super(HealingPotion, self).__init__("HealingPotion", "After you take damage and fight your enemy "
                                                             "take this potion to restore your health"
                                            )


class Shield(Item):
    def __init__(self):
        super(Shield, self).__init__("Shield", "Use this shield to protect "
                                               "yourself from your enemy"
                                     )


class HoverBoard(Item):
    def __init__(self):
        super(HoverBoard, self).__init__("HoverBoard", "You can use this HoverBoard to go "
                                                       "to room to room instead of walking"
                                         )


class Meal(Item):
    def __init__(self):
        super(Meal, self).__init__("Meal", "You can eat this meal at anytime to "
                                           "keep you satisfied while you are in the house.")


class Character(object):
    def __init__(self, name, dialogue, description, health):
        self.name = name
        self.dialogue = dialogue
        self. description = description
        self.health = health
        self.items = []

    def attack(self, target):
        target.health -= 5
        print("%s deals 1 damage" % self.name)

    def interact(self, item):
        self.items += item


player = Character("you", None, "you are the character", 50)
friend = Character("friend", None, "you are my friend", 50)
enemy = Character("enemy", None, "you are my enemy", 50)

if ['punch' 'kick' 'slap']:
    player.attack(enemy)
    print(enemy.health)
    enemy.attack(player)
    print(player.health)


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
attack_methods = ['punch' 'kick' 'slap']
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

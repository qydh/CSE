

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

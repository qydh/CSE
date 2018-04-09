class Character(object):
    def __init__(self, name, dialogue, description, health):
        self.name = name
        self.dialogue = dialogue
        self. description = description
        self.health = health
        self.items = []

    def attack(self, target):
        target.health -= 1
        print("%s deals 1 damage" % self.name)

    def interact(self, item):
        self.items += item


player = Character("you", None, "you are the character", 50)
friend = Character("friend", None, "you are my friend", 50)
enemy = Character("enemy", None, "you are my enemy", 50)
player.attack(enemy)
print(enemy.health)
enemy.attack(player)
print(player.health)
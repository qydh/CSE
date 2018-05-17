# 1 generate number
# create random number

# random number
import random
money = 15
rounds = 0


while money > 0:
    rounds += 1
    dice1 = random.randint(1, 6)
    print(dice1)

    dice2 = random.randint(1, 6)
    print(dice2)

    roll = dice1 + dice2
    print(roll)

    if roll == 7:
        print("you win $4")
        money += 4
    else:
        print("you lost $1")
        money -= 1
    print("You have $%d left" % money)
    print("You played %d rounds" % rounds)
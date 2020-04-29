# Simple DnD or other TableTop RPG Dice roller, First project in Python
# Written by Evan Reeve

from random import randrange

def get_dicenum_and_dicetype():
    # User indicate single dice type and number
    dicenum = 0
    dicetype = 0

    got_valid_input = False

    while not got_valid_input:
        try:
            dicetype_input = input("Choose which dice to roll using the format XdX: ")
            parts = dicetype_input.split("d")
            dicenum = int(parts[0])
            dicetype = int(parts[1])
            got_valid_input = True
        except:
            print("Invalid input. Try again.")

    return dicenum, dicetype


def get_dicemod():
    # User indicate modifiers applied to each die rolled
    dicemod = 0
    got_valid_input = False
    while not got_valid_input:
        try:
            dicemod = int(input("Any modifiers? ex. +3, -1: "))
            got_valid_input = True
        except:
            print("Invalid input. Try again.k")

    return dicemod


def run_dice():
    sumrolls = 0
    total = 0

    dicenum, dicetype = get_dicenum_and_dicetype()
    dicemod = get_dicemod()
    summods = dicemod

    roll_log = []

    # Roll, add indicated modifier, add for total and print results
    for x in range(0, dicenum):
        roll = randrange(1, dicetype + 1)
        totalroll = roll + dicemod
        sumrolls = sumrolls + roll
        total += totalroll

        print("Roll #{0} was {1} ({2} + {3})".format(x + 1, totalroll, roll, dicemod))

    print("Result was: {0}".format(total))

def main():
    print("Hello, adventurer. You must be here to test your luck with dice.\n")

    running = True
    while running:
        run_dice()
        print("Would you like to roll again? (y/n): ")
        running = input() == "y"

    print("Goodbye and see you next time, adventurer!")


main()

#!/usr/bin/env python3
import random
"""
Program is a slot machine that takes a yes or not string from user to play, randomizes 3 numbers, and desides a win 
or a loss.
"""

__author__ = "Nigel Mansell 113208927"
__version__ = "0.0.1"
__license__ = "?"


def main():
    """Entry point"""
    print("Welcome to your slot machine!")
    print("Would you like to play?")
    ans = input("Enter yes or no: ")
    ans = ans.lower()
    ''' If the users answer is yes, fallows through to game, when no or anything else is entered, closes.'''
    if ans == "yes":
        print("Generating numbers...")
        # Leave this for getting your three numbers
        val1 = random.randint(1, 11)
        val2 = random.randint(1, 11)
        val3 = random.randint(1, 11)
        print("You spun: " + str(val1) + " " + str(val2) + " " + str(val3))
        # checks for 3 equal numbers, nested if checks for 3 7s
        if val1 == val2 and val1 == val3:
            if val1 == 7:
                print("Yay!")
                print("You received 750 points!")
            else:
                print("Yay!")
                print("You received 250 points!")
        # checks for equality in first two number, nested if checks those for 7s
        elif val1 == val2:
            if val1 == 7:
                print("Yay!")
                print("You received 100 points!")
            else:
                print("Yay!")
                print("You received 50 points!")
        # checks equality in first and last numbers, nested if checks for 7s
        elif val1 == val3:
            if val1 == 7:
                print("Yay!")
                print("You received 100 points!")
            else:
                print("Yay!")
                print("You received 50 points!")
        # checks equality in last two numbers, nested if checks for 7s
        elif val2 == val3:
            if val2 == 7:
                print("Yay!")
                print("You received 100 points!")
            else:
                print("Yay!")
                print("You received 50 points!")
        # these three elif statements check for individual 7s, no equal numbers.
        elif val1 == 7:
            print("Oh no!")
            print("You received -10 points!")
        elif val2 == 7:
            print("Oh no!")
            print("You received -10 points!")
        elif val3 == 7:
            print("Oh no!")
            print("You received -10 points!")
        else:
            print("Oh no!")
            print("You received -20 points!")
    elif ans == "no":
        print("Goodbye!")
    else:
        print(ans + " is not a valid input! Goodbye!")


if __name__ == '__main__':
    """Executed when run from cmd line"""
    main()

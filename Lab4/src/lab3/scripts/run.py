#!/usr/bin/env python3
import random
"""
Program is a slot machine that takes a yes or not string from user to play, randomizes 3 numbers, and desides a win 
or a loss.
"""

__author__ = "Nigel Mansell 113208927"
__version__ = "0.0.2"
__license__ = "?"


def main():
    """Entry point"""
    print("Welcome to your slot machine!")
    print("Would you like to play?")
    ans = input("Enter yes or no: ")
    ans = ans.lower()
    # loops until a yes or no are entered
    while True:
        if ans != "yes" and ans != "no":
            print("Must enter yes/no: ")
            ans = input("Enter yes or no: ")
            ans = ans.lower()
        else:
            break
    points = 0
    ''' If the users answer is yes, fallows through to game, when no or anything else is entered, closes.'''
    if ans == "no":
        print("Goodbye!")
        return
    elif ans == "yes":
        # loops until user enters no
        while ans != "no":
            if points <= -1000:
                print("You're in too much debt!")
                return
            elif points >= 500:
                print("Know when to quit!")
                return
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
                    points += 750
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return

                else:
                    print("Yay!")
                    print("You received 250 points!")
                    points += 250
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return
            # checks for equality in first two number, nested if checks those for 7s
            elif val1 == val2:
                if val1 == 7:
                    print("Yay!")
                    print("You received 100 points!")
                    points += 100
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return

                else:
                    print("Yay!")
                    print("You received 50 points!")
                    points += 50
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return
            # checks equality in first and last numbers, nested if checks for 7s
            elif val1 == val3:
                if val1 == 7:
                    print("Yay!")
                    print("You received 100 points!")
                    points += 100
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return
                else:
                    print("Yay!")
                    print("You received 50 points!")
                    points += 50
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return
            # checks equality in last two numbers, nested if checks for 7s
            elif val2 == val3:
                if val2 == 7:
                    print("Yay!")
                    print("You received 100 points!")
                    points += 100
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return
                else:
                    print("Yay!")
                    print("You received 50 points!")
                    points += 50
                    print("You now have " + str(points) + " points!")
                    print("Would you like to play again?")
                    ans = input("Enter yes or no: ")
                    ans = ans.lower()
                    # checks for only yes or no
                    while True:
                        if ans != "yes" and ans != "no":
                            print("Must enter yes/no: ")
                            ans = input("Enter yes or no: ")
                            ans = ans.lower()
                        elif ans == "yes":
                            break
                        elif ans == "no":
                            print("Goodbye!")
                            return
            # these three elif statements check for individual 7s, no equal numbers.
            elif val1 == 7:
                print("Oh no!")
                print("You received -10 points!")
                points -= 10
                print("You now have " + str(points) + " points!")
                print("Would you like to play again?")
                ans = input("Enter yes or no: ")
                ans = ans.lower()
                # checks for only yes or no
                while True:
                    if ans != "yes" and ans != "no":
                        print("Must enter yes/no: ")
                        ans = input("Enter yes or no: ")
                        ans = ans.lower()
                    elif ans == "yes":
                        break
                    elif ans == "no":
                        print("Goodbye!")
                        return
            elif val2 == 7:
                print("Oh no!")
                print("You received -10 points!")
                points -= 10
                print("You now have " + str(points) + " points!")
                print("Would you like to play again?")
                ans = input("Enter yes or no: ")
                ans = ans.lower()
                # checks for only yes or no
                while True:
                    if ans != "yes" and ans != "no":
                        print("Must enter yes/no: ")
                        ans = input("Enter yes or no: ")
                        ans = ans.lower()
                    elif ans == "yes":
                        break
                    elif ans == "no":
                        print("Goodbye!")
                        return
            elif val3 == 7:
                print("Oh no!")
                print("You received -10 points!")
                points -= 10
                print("You now have " + str(points) + " points!")
                print("Would you like to play again?")
                ans = input("Enter yes or no: ")
                ans = ans.lower()
                # checks for only yes or no
                while True:
                    if ans != "yes" and ans != "no":
                        print("Must enter yes/no: ")
                        ans = input("Enter yes or no: ")
                        ans = ans.lower()
                    elif ans == "yes":
                        break
                    elif ans == "no":
                        print("Goodbye!")
                        return
            else:
                print("Oh no!")
                print("You received -20 points!")
                points -= 20
                print("You now have " + str(points) + " points!")
                print("Would you like to play again?")
                ans = input("Enter yes or no: ")
                ans = ans.lower()
                # checks for only yes or no
                while True:
                    if ans != "yes" and ans != "no":
                        print("Must enter yes/no: ")
                        ans = input("Enter yes or no: ")
                        ans = ans.lower()
                    elif ans == "yes":
                        break
                    elif ans == "no":
                        print("Goodbye!")
                        return


if __name__ == '__main__':
    """Executed when run from cmd line"""
    main()

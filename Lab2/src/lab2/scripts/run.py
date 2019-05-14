#!/usr/bin/env python3
"""
Module Docstring
"""
__author__ = "Nigel Mansell"
__version__ = "0.0.1"
__license__ = "?"

def myround(x):
    """Takes a variable, rounds, and then returns the rounded variable."""
    numb = int((float(x)*1000)+0.5)/1000
    return numb

def multiply(x):
    """Takes a variable, multiply it by 2, then rounds. Returns variable."""
    numb = int(((float(x)*2)*1000)+0.5)/1000
    return numb

def position(q,l,c,t):
    """Takes 4 variables(quadratic, linear, constant, time), applies math, then returns position."""
    quad = int(((float(t)*float(t)*float(q))*1000)+0.5)/1000
    lin = int(((float(l)*float(t))*1000)+0.5)/1000
    const = myround(c)
    ans = quad + lin + const
    temp = myround(ans)
    return temp

def velocity(q,l,t):
    """Takes 3 variables(quadratic, linear, time), and return velocity."""
    quad = int(((float(t)*multiply(q))*1000)+0.5)/1000
    lin = myround(l)
    ans = quad + lin
    temp = myround(ans)
    return temp

def main():
    """Main entry point"""
    #welcome message
    print("Welcome to my position/velocity calculator!")
    #assigns user input to constant variable
    constant = input("Enter the constant term: ")
    #assigns user intput to linear variable
    linear = input("Enter the linear term: ")
    #assigns user input to quadratic variable
    quadratic = input("Enter the quadratic term: ")
    #outputs to user the position equation after rounding each variable.
    print("The position equation is " + str(myround(quadratic)) + "t^2 + " + str(myround(linear)) + "t + " + str(
        myround(constant)))
    #outputs to user the velocity equation after rounding and rounding appropiatly
    print("The velocity equation is " + str(multiply(quadratic)) + "t + " + str(myround(linear)))
    #assigns user input to time variable
    time = input("Enter a time to calculate: ")
    #outputs to user position at time
    print("The position at time " + str(myround(time)) + " is " + str(position(quadratic,linear,constant,time)))
    #output to user velocity at time
    print("The velocity at time " + str(myround(time)) + " is " + str(velocity(quadratic,linear,time)))
    #end message
    print("Thank you!")

    if __name__ == "__main__":
        """Executed in command line"""
        main()

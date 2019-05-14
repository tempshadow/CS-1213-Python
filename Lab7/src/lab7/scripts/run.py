#!/usr/bin/env python3
'''Nigel Mansell
    Version 0.0.1
    Date: 11/2/18'''

'''Creates and returns a matrix based off user defined rows and columns'''
def creatematrix(row, col):
    a = [0] * row
    for i in range(row):
        a[i] = [0] * col
    # builds matrix based off user specifications and fills with zeroes
    while True:
        # Makes sure user input is a float
        try:
            x = float(input("Enter a value for the matrix or QUIT to stop: "))
            break
        except:
            print("Enter only float values!")
    x = str(x)
    while x.lower() != "quit":
        # Loops until user quit
        while True:
            # makes sure user input for row location is a number, also not out of bounds
            try:
                n_location = int(input("Enter a row location: "))
                if n_location < 0:
                    print("Row location does not exist, must be 0 through " + str(row))
                    continue
                elif n_location > row-1:
                    if row-1 == 0:
                        print("Row location does not exist, must be 0")
                    else:
                        print("Row location does not exist, must be 0 through " + str(row-1))
                    continue
                else:
                    break
            except:
                print("Enter only whole numbers for row location!")
        while True:
            # Same as above, but for column location
            try:
                m_location = int(input("Enter a column location: "))
                if m_location < 0:
                    print("Column location does not exist, must be 0 through " + str(col))
                    continue
                elif m_location > col-1:
                    if col-1 == 0:
                        print("Column location does not exist, myst be 0")
                    else:
                        print("Column location does not exist, must be 0 through " + str(col-1))
                    continue
                else:
                    break
            except:
                print("Enter only whole numbers for column location!")
        if x.lower() != "quit":
            x = float(x)
        a[n_location][m_location] = x
        # places the users value into the user specified location within matrix
        x = input("Enter a value for the matrix or QUIT to stop: ")
    matrixstring = ""
    for i in range(row):
        for j in range(col):
            matrixstring += (str(a[i][j]) + '\t')
        print(matrixstring)
        matrixstring = ""
    # prints values in matrix
    return a

'''Multiplies elements within a matrix. Count is used to keep track of matrix transpose version.'''
def multiply(a, row, col, count):
    while True:
        # Makes sure user input is a float
        try:
            amount = float(input("Amount to multiply by: "))
            break
        except:
            print("Enter only numbers.")
    if count % 2 == 0:
        for i in range(col):
            for j in range(row):
                a[i][j] = a[i][j] * amount
                # multiply value within matrix by user input
    else:
        for i in range(row):
            for j in range(col):
                a[i][j] = a[i][j] * amount
                # same as above

'''Will square all elementes within a matrix. Count keeps track of matrix transpose version.'''
def square(a, row, col, count):
    if count % 2 == 0:
        for i in range(col):
            for j in range(row):
                # Squares values within matrix
                a[i][j] = a[i][j] ** 2
    else:
        for i in range(row):
            for j in range(col):
                # Same as above
                a[i][j] = a[i][j] ** 2

'''Transposes and returns a matrix. Count keeps track of matrix version.'''
def transpose(a, row, col, count):
    if count % 2 == 0:
        # If count is even, will transpose matrix one way, else will transpose matrix the other way
        temp = [0] * row
        for i in range(row):
            temp[i] = [0] * col
        for i in range(row):
            for j in range(col):
                temp[i][j] = a[j][i]
        a = temp
        return a
    else:
        temp = [0] * col
        for i in range(col):
            temp[i] = [0] * row
        for i in range(col):
            for j in range(row):
                temp[i][j] = a[j][i]
        a = temp
        return a

'''Prints matrix depending on the transpose version.'''
def printmatrix(a, row, col, count):
    if count % 2 == 0:
        matrixstring = ""
        for i in range(col):
            for j in range(row):
                matrixstring += (str(a[i][j]) + '\t')
            print(matrixstring)
            matrixstring = ""
    else:
        matrixstring = ""
        for i in range(row):
            for j in range(col):
                matrixstring += (str(a[i][j]) + '\t')
            print(matrixstring)
            matrixstring = ""

'''Runs the program'''
def main():
    print("Welcome to the matrix program!")
    print("Enter the matrix dimensions.")
    while True:
        # Takes input for row amount only if it is a number and that number bust be at last 1
        try:
            n = int(input("Enter number of rows: "))
            if n <= 0:
                print("Must be at least 1")
                continue
            else:
                break
        except:
            print("Enter only whole numbers for rows!")
    while True:
        # Same as above while loop but for column
        try:
            m = int(input("Enter number of columns: "))
            if m <= 0:
                print("Must be at least 1")
                continue
            else:
                break
        except:
            print("Enter only whole numbers for columns")
    a = creatematrix(n, m)
    print("What would you like to do?")
    print("(1) APPLY")
    print("(2) TRANSPOSE")
    print("(3) PRINT")
    print("(4) QUIT")
    while True:
        # Makes sure user only enters 1 2 3 or 4, nothing else
        try:
            choice = int(input("Choice: "))
            if choice < 1:
                print("Must be 1, 2, 3, or 4")
                continue
            elif choice > 4:
                print("Must be 1, 2, 3, or 4")
                continue
            else:
                break
        except:
            print("Enter only numbers.")
    count = 1
    while choice != 4:
        # Loops until choice 4
        if choice == 1:
            print("What would you like to do?")
            print("(1) SQUARE")
            print("(2) MULTIPLY")
            while True:
                # Makes sure user input is an integer that is 1 or 3
                try:
                    choice = int(input("Choice: "))
                    if choice < 1:
                        print("Must be 1 or 2")
                        continue
                    elif choice > 2:
                        print("Must be 1 or 2")
                        continue
                    else:
                        break
                except:
                    print("Enter only numbers")
            if choice == 1:
                square(a, n, m, count)
            elif choice == 2:
                multiply(a, n, m, count)
        elif choice == 2:
            a = transpose(a, n, m, count)
            count += 1
        elif choice == 3:
            # prints values in matrix
            printmatrix(a,n, m, count)
        print("What would you like to do?")
        print("(1) APPLY")
        print("(2) TRANSPOSE")
        print("(3) PRINT")
        print("(4) QUIT")
        while True:
            try:
                choice = int(input("Choice: "))
                if choice < 1:
                    print("Must be 1, 2, 3, or 4")
                    continue
                elif choice > 4:
                    print("Must be 1, 2, 3, or 4")
                    continue
                else:
                    break
            except:
                print("Enter only numbers.")
    print("Goodbye!")
    return


if __name__ == '__main__':
    main()

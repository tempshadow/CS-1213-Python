'''Nigel Mansell 113208927
   version 0.0.1
   date: 10/5/2018'''
def main():
    '''Main function runs colde'''
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
    a = [0] * n
    for i in range(n):
        a[i] = [0] * m
    # lines 30-32 builds matrix based off user specifications and fills with zeroes
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
                    print("Row location does not exist, must be 0 through " + str(n))
                    continue
                elif n_location > n-1:
                    if n-1 == 0:
                        print("Row location does not exist, must be 0")
                    else:
                        print("Row location does not exist, must be 0 through " + str(n-1))
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
                    print("Column location does not exist, must be 0 through " + str(m))
                    continue
                elif m_location > m-1:
                    if m-1 == 0:
                        print("Column location does not exist, myst be 0")
                    else:
                        print("Column location does not exist, must be 0 through " + str(m-1))
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
    for i in range(n):
        for j in range(m):
            matrixstring += (str(a[i][j]) + '\t')
        print(matrixstring)
        matrixstring = ""
    # prints values in matrix
    print("What would you like to do?")
    print("(1) APPLY")
    print("(2) TRANSPOSE")
    print("(3) PRINT")
    print("(4) QUIT")
    while True:
        # Makes suer user only enters 1 2 3 or 4, nothing else
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
                # count keeps track of even or odd due to transpose in main choice 2
                if count % 2 == 0:
                    for i in range(m):
                        for j in range(n):
                            # Squares values within matrix
                            a[i][j] = a[i][j] ** 2
                else:
                    for i in range(n):
                        for j in range(m):
                            # Same as above
                            a[i][j] = a[i][j] ** 2
            elif choice == 2:
                while True:
                    # Makes sure user input is a float
                    try:
                        amount = float(input("Amount to multiply by: "))
                        break
                    except:
                        print("Enter only numbers.")
                if count % 2 == 0:
                    # Works the same as line 127
                    for i in range(m):
                        for j in range(n):
                            a[i][j] = a[i][j] * amount
                            # multiply value within matrix by user input
                else:
                    for i in range(n):
                        for j in range(m):
                            a[i][j] = a[i][j] * amount
                            # same as above
        elif choice == 2:
            if count % 2 == 0:
                # If count is even, will transpose matrix one way, else will transpose matrix the other way
                temp = [0] * n
                for i in range(n):
                    temp[i] = [0] * m
                for i in range(n):
                    for j in range(m):
                        temp[i][j] = a[j][i]
                a = temp
                count += 1
            else:
                temp = [0] * m
                for i in range(m):
                    temp[i] = [0] * n
                for i in range(m):
                    for j in range(n):
                        temp[i][j] = a[j][i]
                a = temp
                count += 1
        elif choice == 3:
            # prints values in matrix
            if count % 2 == 0:
                matrixstring = ""
                for i in range(m):
                    for j in range(n):
                        matrixstring += (str(a[i][j]) + '\t')
                    print(matrixstring)
                    matrixstring = ""
            else:
                matrixstring = ""
                for i in range(n):
                    for j in range(m):
                        matrixstring += (str(a[i][j]) + '\t')
                    print(matrixstring)
                    matrixstring = ""
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


if __name__ == "__main__":
    main()
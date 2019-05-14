#!/usr/bin/env python3
import os
FILE_LOCATION = os.path.join(os.path.dirname(__file__), "../data/data.txt")

__author__ = "Nigel Mansell"
__version__ = "0.0.1"
__date__ = "12/8/2018"


class Map:
    """Map class has a constructor, along with functions import_file, shortest_path, and routes.
        This class calculates the shortest distance between two points defined by a user based off of a graph created
        from the data read in from a file."""
    def __init__(self):
        """Declares and initializes a matrix and a graph."""
        self.matrix = []
        self.Graph = {}

    def import_file(self, file_name):
        """Takes in a file. If file is malformed, the program ends. Stores data into a matrix then uses that matrix
         to fill the graph structure."""
        with open(file_name, "r") as input:
            for line in input:
                try:
                    newline = line.split(',')
                except:
                    print("There was an import error!")
                    return
                temp = newline[2].split('\n')
                self.matrix.append((newline[0], newline[1], str(temp[0])))
        points = []  # Will hold points for the Graph structure.
        for i in range(len(self.matrix)):
            if self.matrix[i][0] not in points:
                points.append(self.matrix[i][0])
            elif self.matrix[i][1] not in points:
                points.append(self.matrix[i][1])
        # Connections will hold all points that a key in the Graph is connected to.
        connections = [[0 for columns in range(len(points))] for rows in range(len(points))]
        count = 0
        for i in range(len(points)):  # Loops through matrix and stores into connections points that link to each key.
            count = 0
            for j in range(len(self.matrix)):
                if self.matrix[j][0] == points[i]:
                    connections[i][count] = self.matrix[j][1]
                    count += 1
                elif self.matrix[j][1] == points[i]:
                    connections[i][count] = self.matrix[j][0]
                    count += 1
        for i in range(len(connections)):  # Removes zeroes only leaving points
            connections[i][:] = (value for value in connections[i] if value != 0)
        for i in range(len(points)):  # Creates the Graph dictionary by using points as keys and connections as values.
            self.Graph[points[i]] = connections[i]

    def shortest_path(self, first, second):
        """Takes in two points. Validates that they exist in the Graph, returning false if they don't.
           Calculates shortest path between points passed in, then outputs path.
           Calculates distance of the shortest path and outputs the distance."""
        if first in self.Graph:
            if second in self.Graph:
                routes = self.routes(first, second)  # calls routes function.
                distances = []
                for i in range(len(routes)):  # Loops through routes, distance becomes 0 each loop.
                    distance = 0
                    for j in range(len(routes[i])):  # Loops through each element within routes.
                        for k in range(len(self.matrix)):  # Loops through matrix.
                            if self.matrix[k][0] == routes[i][j]:  # Looks for an element in a route that is in matrix.
                                if j+1 < len(routes[i]):
                                    if self.matrix[k][1] == routes[i][j+1]:  # Looks for another connection.
                                        distance += int(self.matrix[k][2])  # Updates distance for the current route.
                            elif self.matrix[k][1] == routes[i][j]:  # Does as above but checking opposite connections.
                                if j+1 < len(routes[i]):
                                    if self.matrix[k][0] == routes[i][j+1]:
                                        distance += int(self.matrix[k][2])
                    distances.append(distance)
                smallest = distances[0]  # Variable to hold first element within distances list.
                for i in range(len(distances)):  # Loops through distances to find the smallest distance.
                    if distances[i] < smallest:
                        smallest = distances[i]
                templist = []  # Used to store the smallest distance equally smallest distances.
                for i in range(len(distances)):  # Loops through distances and stores routes that share the distance.
                    if distances[i] == smallest:
                        templist.append(routes[i])
                finallist = [min(templist, key=len)]  # Stores the shortest route if there is another longer route.
                output = [finallist[0], smallest]  # Stores the path and cost for return.
                return output
            else:
                print(second + " does not exist in the structure")
                return None
        else:
            print(first + " does not exist in the structure")
            return None

    def routes(self, start, end, route=[]):
        """Takes in a start and end point to find the all routes."""
        route = route + [start]  # Updates route
        if start == end:
            return [route]  # Returns a route.
        routes = []
        for node in self.Graph[start]:  # Loops through values of a the given key [start]
            if node not in route:
                newroutes = self.routes(node, end, route)  # newroutes becomes the return value of the recursive call.
                for newroute in newroutes:
                    routes.append(newroute)
        return routes  # Returns all routes that go from starting point to the end point.


def main():
    """Runs the program by creating map objects, calling maps functions, and getting user input."""
    map = Map()
    map.import_file(FILE_LOCATION)
    first = input("Enter a start location: ").upper()
    second = input("Enter end location: ").upper()
    while True:  # Infinite loop until user enters yes.
        temp = map.shortest_path(first, second)  # Calls shortest_path.
        if temp == None:
            first = input("Enter a start location: ").upper()
            second = input("Enter end location: ").upper()
            continue
        else:
            out = first
            for i in range(1, len(temp[0])):  # Loops through list starting at index 1 to combine its elements to out.
                out += "->" + temp[0][i]
            print("Path: " + out)
            print("Cost: " + str(temp[1]))
        quit = input("Quit? ")
        while True:  # Infinite loops until user enters yes.
            if quit.lower() == "yes":
                print("Goodbye")
                return
            elif quit.lower() == "no":
                first = input("Enter a start location: ").upper()
                second = input("Enter end location: ").upper()
                break
            else:
                print("Must be yes or no.")
                quit = input("Quit? ")


if __name__ == '__main__':  # Looks for main and runs it.
    main()

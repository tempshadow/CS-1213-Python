import os
FILE_LOCATION = os.path.join(os.path.dirname(__file__), "../data/friends.txt")
POST_FILE_LOCATION = os.path.join(os.path.dirname(__file__), "../data/posts.txt")
LOGIN_MENU = "What would you like to do?\n1. Login\n2. Create Account"
MAIN_MENU = "What would you like to do?\n1. Add friend\n2. Create post\n3. See friend's posts\n4. Quit"

class User():
    userName = "/"
    password = "/"
    age = 0
    email = "/"
    def __init__(self, userName, age, password, email):
        self.userName = userName
        self.password = password
        self.age = age
        self.email = email

class SocialGraph():
    userList = []  # holds all users
    friendList = []  # holds the friends relations
    postList = []
    currentUser = User("/", 0, "/", "/")  # Just declaring an empty object to be used
    def __init__(self):
        print("\n")
    def import_file(self,file):
        fileToOpen = open(file, 'r')
        f = fileToOpen.read()
        fileToOpen.close()
        lines = f.split("\n")
        secondHalf = False
        if file == FILE_LOCATION:
            # Users and friends
            for line in lines:
                if ("--" in line):
                    secondHalf = True
                    continue
                if (secondHalf == False):
                    splitLine = line.split(",")
                    name = splitLine[0]
                    age = int(splitLine[1])
                    password = splitLine[2]
                    email = splitLine[3]
                    newFriend = User(name, age, password, email)
                    self.userList.append(newFriend)
                if (secondHalf == True):
                    self.friendList.append(line)
        elif file == POST_FILE_LOCATION:
            for line in lines:
                self.postList.append(line)

    def export_file(self,file):
        f = open(file, 'w')
        if (file == FILE_LOCATION):
            for user in self.userList:
                f.write(user.userName + "," + str(user.age) + "," + user.password + "," + user.email + "\n")
            f.write("--\n")

            for friendDuo in self.friendList:
                f.write(friendDuo + "\n")
            f.close()
        elif (file == POST_FILE_LOCATION):
            #f = open(file, 'w')
            for post in self.postList:
                f.write(post + "\n")
            f.close()

    def login_user(self):
        inputName = input("Username: ")
        inputPassword = input("Password: ")
        accountFound = False
        for user in self.userList:
            if (user.userName == inputName):
                if (user.password == inputPassword):
                    accountFound = True
                    print("login successful")
                    self.currentUser = user
                    return True
        if (accountFound == False):
            print("Incorrect user name or password")
            return False

    def create_user(self):
        newUserName = input("Enter username: ")
        newUserAge = 0
        ageLoop = True
        while ageLoop:
            newUserAgeInput = input("Enter user age: ")
            if newUserAgeInput.isnumeric():
                ageLoop = False
                newUserAge = int(newUserAgeInput)
            else:
                print("Age must be a number")
        newUserPassword = ""
        newUserEmail = ""
        passwordLoop = True
        while passwordLoop:
            newUserPassword = input("Enter user password: ")
            confirmPassword = input("Confirm password: ")
            if (newUserPassword != confirmPassword):
                print("passwords did not match")
            elif (newUserPassword == confirmPassword):
                passwordLoop = False
        emailLoop = True
        while emailLoop:
            newUserEmail = input("Enter user email: ")
            if "@" in newUserEmail:
                emailLoop = False
            else:
                print("Email must contain an '@' symbol")
        userAlreadyExists = False
        for user in self.userList:
            if newUserName in user.userName:
                print("User already exists")
                userAlreadyExists = True
                break
        if userAlreadyExists == False:
            newUser = User(newUserName, newUserAge, newUserPassword, newUserEmail)
            currentUser = newUser
            self.userList.append(currentUser)
        self.export_file(self, FILE_LOCATION)#saves user

    def add_friend(self):
        userInput = input("Enter a new friend name: ")
        alreadyFriends = False
        friendExists = False
        for user in self.userList:  # checks to see if user even exists
            if userInput in user.userName:
                friendExists = True
        for friends in self.friendList:  # checks to see if already friends
            if (userInput in friends and self.currentUser.userName in friends):
                alreadyFriends = True
                break
        if alreadyFriends == False:
            if friendExists == True:
                self.friendList.append(self.currentUser.userName + "," + userInput)  # Add friend
            elif friendExists == False:
                print("User to add as friend does not exist")
        else:
            print("User is already friends with " + userInput)
        self.export_file(self, FILE_LOCATION)

    def create_post(self):
        postInput = input("Enter post text: ")
        postName = self.currentUser.userName + ","
        self.postList.append(postName + postInput)
        self.export_file(self, POST_FILE_LOCATION)

    def get_friends_posts(self):
        postInput = input("Enter friend name: ")
        alreadyFriends = False
        for friends in self.friendList:  # checks to see if already friends
            if (postInput in friends and self.currentUser.userName in friends):
                alreadyFriends = True
                break
        if (alreadyFriends == True):
            for post in self.postList:
                if postInput in post:
                    postSplit = post.split(",")
                    print(postSplit[1])
        else:
            print("Cannot display. You are not friends with this user.")

def main():
    socialGraph = SocialGraph
    print("Welcome to the social media application!")
    socialGraph.import_file(SocialGraph, FILE_LOCATION)
    socialGraph.import_file(SocialGraph, POST_FILE_LOCATION)
    programControl = True
    while(programControl):
        userInput = input(LOGIN_MENU)
        if (userInput == "1"):
            loginSuccess = socialGraph.login_user(SocialGraph)
            if loginSuccess == True:
                while (programControl):
                        userInput = input(MAIN_MENU)
                        if (userInput == "1"):
                            socialGraph.add_friend(SocialGraph)
                        elif (userInput == "2"):
                            socialGraph.create_post(SocialGraph)
                        elif (userInput == "3"):
                            socialGraph.get_friends_posts(SocialGraph)
                        elif (userInput == "4"):
                            print("Goodbye!")
                            programControl = False
                            break
                        else:
                            print("incorrect input")
        elif (userInput == "2"):
            socialGraph.create_user(SocialGraph)
            continue
        else:
            print("Incorrect Input. Enter 1 or 2")
            continue

if __name__ == '__main__':
    main()
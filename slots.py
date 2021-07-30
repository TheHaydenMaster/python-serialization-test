import pickle                                                                   #import libraries
import random

users = {}                                                                      #create an empty users dictionary

baseWalletAmount = 100

serialize_users = pickle.dumps(users)                                                       #Sets the value added to a new users account upon creation

def createUser():
    get_username =  str(input("Please Enter a Username: "))
    users[get_username] = baseWalletAmount
    print("Succesfully Created User!")

def runGame():
    startUp = str(input("Press the Key Corresponding with the Selection of the option you want \n0 - Create User \n1 - Login User \nEnter Selection: "))
    try:
        pickle.loads(serialize_users)
    except NameError:
        print("Couldn't Load Users!")

    if startUp == "0":
        createUser()
        runGame()
    elif startUp == "1":
        print("WIP - Come Back Soon!")
    elif startUp == "2":
        print(users)
        runGame()
    else:
        runGame()

runGame()

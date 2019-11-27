#Manfred Tan - Team Jacket
#SoftDev pd9
#P01
#2019-11-19

import sqlite3
import csv

######################################################################################################
######################################################################################################
######################################################################################################

def createUserTable():
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # Creates the user database: username|password|decks
    command = "CREATE TABLE IF NOT EXISTS users (userID INTEGER, username TEXT, password TEXT NOT NULL, PRIMARY KEY (userID, username));"
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database

def createHockeyTable():
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # Creates the user database: username|password|decks
    command = "CREATE TABLE IF NOT EXISTS hockey (name TEXT PRIMARY KEY, health INT NOT NULL, attack INT NOT NULL, image TEXT);"
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database

def createPokemonTable():
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # Creates the user database: username|password|decks
    command = "CREATE TABLE IF NOT EXISTS pokemon (name TEXT PRIMARY KEY, element TEXT NOT NULL, image TEXT);"
    c.execute(command)
    db.commit() #save changes
    db.close()  #close database

######################################################################################################
######################################################################################################
######################################################################################################

def login(user_username, user_password):
    # RETURNS:
    # valid userID.
    # If doesn't exist, return -1
    #==============
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    num = -1
    findUser = "SELECT * FROM users WHERE username='" + user_username + "' and password='" + user_password + "';"
    data = c.execute(findUser) # returns user's data
    for row in data:
        num = row[0]
    db.commit() #save changes
    db.close()  #close database
    return(num)

def register(user_username, user_password1, user_password2):
    # RETURNS:
    # -1 for existing username
    # -2 for passwords do not match
    # -3 for password not over 5 characters
    # if valid returns userID
    #==============
    # checks if username exists or passwords incorrect then makes new user
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #USERNAME EXISTS?
    checkUsername = "SELECT username FROM users WHERE username='" + user_username + "';"
    data = c.execute(checkUsername)
    for row in data:
        if (user_username == row[0]):
            return(-1)
    # PASSWORDS MATCH?
    if (user_password1 != user_password2):
        return(-2)
    # PASSWORD LENGTH?
    if (len(user_password1) < 5):
        return(-3)
    # ADD USER TO DATABASE !
    getNextID = "SELECT userID FROM users;"
    data = c.execute(getNextID)
    num = 1;
    for ID in data:
        num += 1
    command = "INSERT INTO users VALUES (" + str(num) + ",'" + user_username + "', '" + user_password1 + "');"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database
    return(num)

######################################################################################################
######################################################################################################
######################################################################################################

def addHockey(name,health,attack,image):
    #INSERT INTO hockey VALUES ('name', 100, 25, 'img');
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #Adding hockey players
    addHockey = "INSERT INTO hockey VALUES (\'" + name + "\', " + str(health) + ", " + str(attack) + ", \'" + image + "\'" + ");"
    data = c.execute(addHockey)
    db.commit() #save changes
    db.close()  #close database
    print( "Inserted: " + name + ", " + str(health) + ", " + str(attack) + ", " + image)
    return(True)

def addPokemon(name,element,image):
    #INSERT INTO hockey VALUES ('name', 100, 25, 'img');
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #Adding hockey players
    addPokemon = "INSERT INTO pokemon VALUES (\'" + name + "\', \'" + element + "\', \'" + image + "\'" + ");"
    data = c.execute(addPokemon)
    db.commit() #save changes
    db.close()  #close database
    print( "Inserted: " + name + ", " + element + ", " + image)
    return(True)

######################################################################################################
######################################################################################################
######################################################################################################

def chooseHockey():
    return(True)

def choosePokemon():
    return(True)

######################################################################################################
######################################################################################################
######################################################################################################

def showAll():
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    ###
    listOfCharacters = []
    listOfHockey = []
    listOfPokemon = []
    ###
    displayHockey = "SELECT * FROM hockey;"
    data = c.execute(displayHockey)
    for row in data:
        listOfHockey.append(row)
    ###
    displayPokemon = "SELECT * FROM pokemon;"
    data = c.execute(displayPokemon)
    for row in data:
        listOfPokemon.append(row)
    ###
    listOfCharacters.append(listOfHockey)
    listOfCharacters.append(listOfPokemon)
    print("Returns: " + str(listOfCharacters))
    print("listOfCharacters[0][0]: " + str(listOfCharacters[0][0]))
    print("listOfCharacters[0][0][0]: " + listOfCharacters[0][0][0])

    return(listOfCharacters)


#addHockey("Lebron James", 500, 150, "jamesL.png")
#addHockey("Manfred Tan", 300, 15, "tanM.png")


#createTable()
#register('admin', 'admin', 'admin')

#Manfred Tan - Team Jacket
#SoftDev pd9
#P01
#2019-11-19

import sqlite3
import csv

def createTable():
    DB_FILE="../database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # Creates the user database: username|password|decks
    command = "CREATE TABLE IF NOT EXISTS users (userID INTEGER, username TEXT, password TEXT NOT NULL, PRIMARY KEY (userID, username));"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database


def login(user_username, user_password):
    # returns userID. If DNE, return -1
    DB_FILE="../database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    findUser = "SELECT * FROM users WHERE username='" + user_username + "' and password='" + user_password + "';"
    data = c.execute(findUser) # returns user's data
    for row in data:
        print(row[0])
    db.commit() #save changes
    db.close()  #close database


def register(user_username, user_password1, user_password2):
    # checks if username exists or passwords incorrect then makes new user
    DB_FILE="../database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #check username existence
    checkUsername = "SELECT * FROM users WHERE username='" + user_username + "';"
    data = c.execute(checkUsername)
    for row in data:
        if (user_username == row[0]):
            print(False)
    #check password match
    if (user_password1 != user_password2):
        print(False)
    #add user
    
    addUser = "INSERT INTO users VALUES (\'user_username\', \'user_password1\');"
    data = c.execute(addUser)
    getUserID = "SELECT userID FROM users WHERE username=\'user_username\';"
    print(getUserID)

createTable()

register('admin', 'pass', 'pass')

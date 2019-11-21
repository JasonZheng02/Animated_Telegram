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
    command = "CREATE TABLE IF NOT EXISTS users (userid INTEGER, username TEXT, password TEXT NOT NULL, decks VARCHAR, PRIMARY KEY (userid, username));"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database


def checkLogin(user_username, user_password):

    DB_FILE="../database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    command = "SELECT * FROM users WHERE username='" + user_username + "' and password='" + user_password + "';"
    temp = c.execute(command)
    for row in temp:
        print(row)


    db.commit() #save changes
    db.close()  #close database


checkLogin('manfred', 'tanx')

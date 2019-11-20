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
    command = "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL, decks VARCHAR);"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database


def tester1():

    #pip install -r req.txt
    #SELECT * FROM users WHERE password='password';
    
    DB_FILE="../database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    command = ""

    db.commit() #save changes
    db.close()  #close database

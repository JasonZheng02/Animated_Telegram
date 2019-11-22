#Manfred Tan
#SoftDev
#P1

import sqlite3
import csv

def checkLogin(username, password):
    #returns userid of the username, password pair. returns -1 if it doesn't exist
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #======================================
    command = "SELECT user_id, username FROM users WHERE username = \"{}\" AND password = \"{}\";".format(username, password) #looks for the username,password combination in the users db
    c.execute(command)
    q = c.fetchall()
    #======================================

    db.commit() #save changes
    db.close()  #close database

    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    if q[0][0] == "" or q[0][1] == "": #doesn't allow for username or password to be empty
        return -1
    else:
        return q[0][0] #return ID of user if exists

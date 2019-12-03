#Manfred Tan - Team Jacket
#SoftDev pd9
#P01
#2019-11-19

import sqlite3
import csv
from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os
import urllib.request as urlrequest
from urllib.request import urlopen, Request
import json

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


def yurd():
    DB_FILE="database/databases.db"
    url = urlopen("https://records.nhl.com/site/api/player/byTeam/1")
    response = url.read()
    data = json.loads(response)
    data = data["data"]
    x = 0
    id = []
    name = []
    height = []
    weight = []
    nhl = []
    pokemon = ["pikachu", "bulbasaur", "charmander", "squirtle", "turtwig"]
    pokemonType = []
    DB_FILE = "database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='chars' ''')
    if c.fetchone()[0] < 1:
        c.execute("CREATE TABLE chars(name TEXT, attack INT, defense INT, type TEXT);")
        while (x < 50):
            id.append(data[x]["id"])
            url = urlopen("https://statsapi.web.nhl.com/api/v1/people/" + str(id[x]))
            response = url.read()
            data2 = json.loads(response)
            data2 = data2["people"][0]
            name.append(data2["fullName"])
            height.append(data2["height"])
            weight.append(data2["weight"])
            x = x + 1
        for x in pokemon:
            req = Request("https://pokeapi.co/api/v2/pokemon/" + str(x), headers = {'User-Agent': 'Mozilla/5.0'})
            link = urlopen(req)
            response = link.read()
            data = json.loads(response)
            pokemonType.append(data["types"][0]["type"]["name"])
        x = 0
        with sqlite3.connect(DB_FILE) as db:
            c = db.cursor()
            while (x < 50):
                c.execute('INSERT INTO chars VALUES (?, ?, ? ,?)', (name[x], height[x], weight[x], 'hockey'))
                nhl.append(" " + str(name[x]) + ", " + str(height[x]) + ", " + str(weight[x]) + " ")
                x = x + 1

            for i in range(5):
                c.execute('INSERT INTO chars VALUES (?, ?, ?, ?)', (pokemon[i], 0,0, pokemonType[i]))
            c.execute('SELECT * FROM chars')
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='decks' ''')
    if c.fetchone()[0] < 1:
        s = "CREATE TABLE decks(user TEXT, deckname TEXT,"
        for i in range(15):
            s += "char" + str(i) + " TEXT" + ","
        c.execute(s[:len(s) - 1] + ");")



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

def decks(decks_username, decks_deckname):
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
    #c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='decks' ''')
    checkDeck = "SELECT name FROM decks WHERE username='" + decks_username + "';"
    data = c.execute(checkDeck)
    for row in data:
        if (decks_deckname in row):
            return(-1)
    # PASSWORDS MATCH?
    if(decks_deckname == ""):
        return(-2)
    # ADD USER TO DATABASE !


    db.commit() #save changes
    db.close()  #close database
    return(num)
######################################################################################################
######################################################################################################
######################################################################################################



######################################################################################################
######################################################################################################
######################################################################################################

def chooseHockey(name):
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    findHockey = "SELECT * FROM hockey WHERE name=\'" + name + "\';"
    data = c.execute(findHockey)
    player = []
    for row in data:
        print("Character in list form: " + str(row))
        return(row)

def choosePokemon(name):
    DB_FILE="database/databases.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    findPokemon = "SELECT * FROM pokemon WHERE name=\'" + name + "\';"
    data = c.execute(findPokemon)
    player = []
    for row in data:
        print("Character in list form: " + str(row))
        return(row)

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

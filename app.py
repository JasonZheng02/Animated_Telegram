# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os
from database import setupDB
import urllib.request as urlrequest
from urllib.request import urlopen, Request
import json

##################################################################################
setupDB.createUserTable()
setupDB.yurd()
DB_FILE="database/databases.db"

    #print(len(c.fetchall()))

################################################################################################################
app = Flask(__name__)
app.secret_key = os.urandom(32) #generates secret key for session

nameDecks = ""
decknumber = 0
currentDeck=[]

@app.route("/")
def dock():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if (request.form):
        print(True)
        session['username'] = request.form["username"]  # assign username key in session to inputted username
        session['password'] = request.form["password"]  # assign password key in session to inputted password
        getID = setupDB.login(session['username'], session['password'])
        session['userID'] = getID
        if (getID == -1):
            return render_template('login.html', errorMessage = "Invalid Credentials")
        print("User: " + session['username'])
        print("ID: " + str(session['userID']))
        return redirect(url_for("main"))
    else:
        return render_template('login.html',errorMessage = "")

@app.route("/register", methods=["POST"])
def register():
    errorMessage=""
    if (request.form):
        session['username'] = request.form["username"]  # assign username key in session to inputted username
        session['password1'] = request.form["password1"]  # assign username key in session to inputted username
        session['password2'] = request.form["password2"]  # assign username key in session to inputted username
        createID = setupDB.register( request.form["username"], request.form["password1"], request.form["password2"])
        session['userID'] = createID
        if (createID == -1):
            errorMessage="Username already exists"
        if (createID == -2):
            errorMessage="Passwords do not match"
        if (createID == -3):
            errorMessage="Password must be greater than 5 characters"
        if (createID >= 0):
            print("New User: " + session['username'])
            print("ID: " + str(session['userID']))
            return redirect(url_for("main"))
    return render_template('register.html', errorMessage=errorMessage)


@app.route("/nameDeck", methods=["GET", "POST"])
def nameDeck():
    #print(111111111111111111111111111111111111111111111111111111111111111111111111111111111)
    global currentDeck
    currentDeck = []
    if(request.form):
        print(111111111111111111111111111111111111111111111111111111111111111111111111111111111)
        global nameDecks
        nameDecks = request.form["deckName"]
                 # assign password key in session to inputted
    return render_template("nameDeck.html", user=session['username'])


@app.route("/main")
def main():
    return render_template("main.html", user=session['username'])

@app.route('/addtodeck/<deck_name>/<card_name>', methods = ["GET","POST"])
def add_to_deck(deck_name, card_name):
    global currentDeck
    if(len(currentDeck)>15):
        return redirect('/makeDeck')
    currentDeck.append(card_name)
    return redirect('/makeDeck')

@app.route('/removefromdeck/<deck_name>/<card_name>')
def removefromdeck(deck_name, card_name):
    global currentDeck
    if(len(currentDeck)<1):
        return redirect('/makeDeck')
    currentDeck.remove(card_name)
    return redirect('/makeDeck')

@app.route('/editdeck/<deck_name>')
def edit_deck(deck_name):
    global currentDeck
    currentDeck = deckName
    return redirect('/makeDeck')

@app.route("/makeDeck", methods = ["POST", "GET"])
def makeDeck():
    global nameDecks
    print(nameDecks)
    global currentDeck
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        c.execute('SELECT * FROM chars')
        players = c.fetchall()

    #we also need to make a deck maker string, that we will evenetually loop through and add to the decks database
    return render_template("makeDeck.html",  players = players, deck = currentDeck)

@app.route("/chooseDeck")
def chooseDeck():
    return render_template("chooseDeck.html")

@app.route("/victory")
def victory():
    return render_template("victory.html")

@app.route("/defeat")
def defeat():
    return render_template("defeat.html")

@app.route("/playScreen")
def playScreen():
    return render_template("playScreen.html")



if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port = '5000', debug = True)

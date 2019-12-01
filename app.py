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
DB_FILE = "database/databases.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='chars' ''')
if c.fetchone()[0] < 1:
    c.execute("CREATE TABLE chars(name TEXT, attack INT, defense INT, type TEXT);")
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='decks' ''')
if c.fetchone()[0] < 1:
    s = "CREATE TABLE decks(user TEXT, deckname INT,"
    for i in range(30):
        s += "char" + str(i) + " TEXT" + ","
    c.execute(s[:len(s) - 1] + ");")

################################################################################################################
app = Flask(__name__)
app.secret_key = os.urandom(32) #generates secret key for session

decknumber = 0
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

@app.route("/main")
def main():
    return render_template("main.html", user=session['username'])


@app.route("/makeDeck")
def makeDeck():
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
    pokemon = ["pikachu", "bulbasaur", "charmander", "squirtle"]
    pokemonType = []
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
    while (x < 50):
        nhl.append(" " + str(name[x]) + ", " + str(height[x]) + ", " + str(weight[x]) + " ")
        x = x + 1
    return render_template("makeDeck.html", nhl = nhl, pokemon = pokemon, pokemonType = pokemonType)

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
	app.run()

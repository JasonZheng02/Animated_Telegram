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

DB_FILE = "database/databases.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='userdata' ''')
if c.fetchone()[0] < 1:
    c.execute("CREATE TABLE chars(name TEXT, attack INT, defense INT, type TEXT);")
    #the power will literally be the sum of the height and weight



app = Flask(__name__) #create instance of class Flask

@app.route('/')
def home():
    url = urlopen("https://records.nhl.com/site/api/player/byTeam/1")
    response = url.read()
    data = json.loads(response)
    print(data)
    data = data["data"]
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        #otherwise insert the new blog into the blog databaset
        c.execute('''INSERT INTO blogdata VALUES (?, ?, ?, ?)''', (None, session["username"], "" + request.args["title"], "" + request.args["body"]))
        return redirect("/Main")
    x = 0
    id = []
    name = []
    pokemon = []
    while (x < 50):
        id.append(data[x]["id"])
        url = urlopen("https://statsapi.web.nhl.com/api/v1/people/" + str(id[x]))
        response = url.read()
        data2 = json.loads(response)
        data2 = data2["people"][0]
        name.append(data2["fullName"])
        x = x + 1
    req = Request("https://pokeapi.co/api/v2/pokemon/pikachu", headers = {'User-Agent': 'Mozilla/5.0'})
    link = urlopen(req)
    response = link.read()
    data = json.loads(response)
    return render_template("makeDeck.html", d = id, name = name, pokemon = data)


if __name__ == "__main__":
	app.debug = True
	app.run()

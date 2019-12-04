# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os
import random
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
yourDeck = []
yourLives = 3
compLives = 3

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
    errorMessage = "Don't pick an existing name!"
    #print(111111111111111111111111111111111111111111111111111111111111111111111111111111111)
    global currentDeck
    global nameDecks
    currentDeck = []
    if(request.form):
        #print(111111111111111111111111111111111111111111111111111111111111111111111111111111111)
        with sqlite3.connect(DB_FILE) as db:
            c = db.cursor()
            c.execute("SELECT deckname FROM decks WHERE user = '" + session["username"] + "' AND deckname = '" +  request.form["deckName"] + "';")
            if (not len(c.fetchall()) == 0) or request.form["deckName"] == "":
                errorMessage = "Name Taken or empty form"
                print(request.form["deckName"] + "11111111111111111111111")
                return render_template("nameDeck.html", user=session['username'], errorMessage = errorMessage)
        nameDecks = request.form["deckName"]
        #print(nameDecks + "77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777")
                 # assign password key in session to inputted

        print("2222222222222222")
        return redirect('/makeDeck')
    return render_template("nameDeck.html", user=session['username'], errorMessage = errorMessage)

@app.route("/main")
def main():
    findDeck('crazy')
    hdr = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request("https://deckofcardsapi.com/api/deck/new/draw/?count=3", headers=hdr)
    link = urlopen(req)
    response = link.read()
    data = json.loads( response )
    img0 = data["cards"][0]["images"]["png"]
    print(img0)
    print("IMAGE0 ^")
    img1 = data["cards"][1]["images"]["png"]
    img2 = data["cards"][2]["images"]["png"]

    return render_template("main.html", user=session['username'], img0 = img0, img1=img1, img2=img2)

@app.route('/gameDeck/<deck_name>')
def gameDeck(deck_name):
    global yourDeck
    yourDeck = findDeck(deck_name)
    return redirect('/gamePage')

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
    #currentDeck = deckName
    return redirect('/makeDeck')

@app.route('/newDeck')
def newDeck():
    global nameDecks
    global currentDeck
    print(nameDeck)
    temp = [session["username"], nameDecks]
    #ok we have to add this to the database now
    for i in currentDeck:
        temp.append(i)
    b = tuple(temp)
    print(b)
    #I WILL MOVE THE BELOW FUNCTION TO THE DB.PY file after it is finalized
    DB_FILE="database/databases.db"
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        #this will be a useful string
        #17 entries, all the chars + user and deckName a the front

        c.execute("INSERT INTO decks VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", b)
        print(c.fetchall())
    return redirect('/main')

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
    return render_template("makeDeck.html",  players = players, deck = currentDeck, l = len(currentDeck))



@app.route("/chooseDeck")
def chooseDeck():
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        c.execute("SELECT * FROM decks WHERE user = '" + session["username"] + "';")
        stuff = c.fetchall()
        names = []
        for i in stuff:
            names.append(i)
        return render_template("chooseDeck.html", players = names)

def findDeck(name):
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        c.execute("SELECT * FROM decks WHERE user = '" + session["username"] + "'" + "AND deckname = '" + name + "';")
        stuff = c.fetchall()
        #stuff = stuff[2:]
        listOfNames = stuff[0][2:]
        finalDeck = []
        for person in listOfNames:
            c.execute("SELECT * FROM chars WHERE name = '" + person + "';")
            temp = c.fetchall()[0]
            finalDeck.append(temp)
        print('***************')
        print(finalDeck)
        return finalDeck

@app.route("/victory")
def victory():
    return render_template("victory.html")

@app.route("/defeat")
def defeat():
    return render_template("defeat.html")

@app.route("/playScreen")
def playScreen():
    return render_template("playScreen.html")

@app.route("/gamePage", methods=["GET", "POST"])
def gamePage():
    global yourLives
    global compLives
    global yourDeck
    global yourCard

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM chars;"
    c.execute(command)
    computerDeck = c.fetchall()

    print("LOOK AT THIS !!!!")

    if (yourLives == 0):
        yourLives = 3
        compLives = 3
        return render_template('defeat.html')
    if (compLives == 0):
        yourLives = 3
        compLives = 3
        return render_template('victory.html')

    return render_template('gamePage.html',
        yourDeck = yourDeck,
        g = random.sample(population = range(len(yourDeck)),k=3),
        yourLives = yourLives,
        compLives = compLives,
        message = "NOTHING HERE")


@app.route('/gamePageFight')
def gamePageFight():

    global yourLives
    global compLives
    global yourDeck
    global yourCard

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM chars;"
    c.execute(command)
    computerDeck = c.fetchall()

    print(yourCard[3]) #chooseCard(userDeck)

    compCard = computerDeck[random.randint(0,54)]
    #####
    print(compCard[3])
    ########################
    #FIGHT
    battle = True
    if (not yourCard[3] == "hockey") and (compCard[3] == "hockey"):
        battle == True
    if (not compCard[3] == "hockey") and (yourCard[3] == "hockey"):
        battle == False
    ##########################
    if(compCard[3] == "hockey" and yourCard[3] == "hockey"):
        #weighted average time
        compTotal = int(compCard[1].split()[0][0]) * 12 + int(compCard[1].split()[1][0]) + compCard[2]
        yourTotal = int(yourCard[1].split()[0][0]) * 12 + int(yourCard[1].split()[1][0]) + yourCard[2]
        if(yourTotal > random.randint(0, yourTotal + compTotal)):
            battle = True
        else:
            battle = False
    ###pokemon case
    if not (compCard[3] == "hockey" or yourCard[3] == "hockey"):
         ###casework
         if yourCard[3] == "pikachu":
             if(compCard[3] == "squirtle" or compCard[3] == "charmander"):
                 battle = True
             elif(compCard[3] == "turtwig" or compCard[3] == "bulbasaur"):
                 battle = False
             else:
                 battle = random.choose([True, False])
         if yourCard[3] == "charmander":
             if(compCard[3] == "turtwig" or compCard[3] == "bulbasaur"):
                 battle = True
             elif(compCard[3] == "squirtle" or compCard[3] == "pikachu"):
                 battle = False
             else:
                 battle = random.choose([True, False])
         if yourCard[3] == "bulbasaur":
             if(compCard[3] == "turtwig" or compCard[3] == "squirtle" or compCard[3] == "pikachu"):
                 battle = True
             elif(compCard[3] == "charmander"):
                 battle = False
             else:
                 battle = random.choose([True, False])
         if yourCard[3] == "turtwig":
             if (compCard[3] == "squirtle" or compCard[3] == "pikachu"):
                 battle = True
             elif(compCard[3] == "charmander" or compCard[3] == "bulbasaur"):
                 battle = False
             else:
                 battle = random.choose([True, False])
         if yourCard[3] == "squirtle":
             if (compCard[3] == "charmander"):
                 battle = True
             elif(compCard[3] == "turtwig" or compCard[3] == "bulbasaur" or compCard[3] == "pikachu"):
                 battle = False
             else:
                 battle = random.choose([True, False])

    if (battle == True):
        compLives -= 1
        return render_template('gamePageFight.html',
            yourDeck = yourDeck,
            g = random.sample(population = range(len(yourDeck)),k=3),
            yourLives = yourLives,
            compLives = compLives,
            yourCard = yourCard,
            compCard = compCard,
            message = "YOU WON!")
    else:
        yourLives -= 1
        return render_template('gamePageFight.html',
            yourDeck = yourDeck,
            g = random.sample(population = range(len(yourDeck)),k=3),
            yourLives = yourLives,
            compLives = compLives,
            yourCard = yourCard,
            compCard = compCard,
            message = "YOU LOST!")


yourCard = ()

@app.route('/choosePlayer/<tup>')
def choosePlayer(tup):
    print(tup)
    player = int(tup)
    print(player)
    global yourCard
    yourCard = yourDeck[player]
    print(yourCard)
    yourDeck.remove(yourDeck[int(tup)])
    return(redirect("/gamePageFight"))



if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port = '5000', debug = True)

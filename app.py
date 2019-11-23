# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os
from database import setupDB

################################################################################################################
app = Flask(__name__)
app.secret_key = os.urandom(32) #generates secret key for session

@app.route("/")
def dock():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if (request.form):
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
    return render_template("makeDeck.html")

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

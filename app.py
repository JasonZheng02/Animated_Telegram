# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os

################################################################################################################
app = Flask(__name__)
app.secret_key = os.urandom(32) #generates secret key for session

@app.route("/")
def login():
    return render_template("login.html")
    #    if ('username' not in session or 'password' not in session):
    #        redirect(url_for("login"))

@app.route("/loginHelper", methods=["POST"])
def login1():
    session['username'] = request.form["username"]  # assign username key in session to inputted username
    session['password'] = request.form["password"]  # assign password key in session to inputted password
    if (session):
        username = session['username']
        password = session['password']
        checkLogin = checkLogin.checkLogin(username, password)
        if (checkLogin == -1):
            return render_template('login.html', errorMessage = "Invalid Credentials")
        return redirect(url_for("home"))
    else:
        return render_template('login.html',errorMessage = "")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
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

# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os

################################################################################################################
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
	app.debug = True
	app.run()

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

app = Flask(__name__) #create instance of class Flask

@app.route('/')
def home():

    req = Request("https://pokeapi.co/api/v2/pokemon/", headers={'User-Agent': 'Mozilla/5.0'})
    link = urlopen(req)
    response = link.read()
    data = json.loads( response )

    results = data['results']

    return(data)


if __name__ == "__main__":
	app.debug = True
	app.run()

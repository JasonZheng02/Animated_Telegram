# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
import os
from database import setupDB
import urllib.request as urlrequest
from urllib.request import urlopen
import json



def testAddPokemon():
    return(setupDB.addPokemon('manfred', 'fire', 'manfred.jpeg'))


testAddPokemon()

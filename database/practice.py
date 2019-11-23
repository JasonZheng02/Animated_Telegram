import sqlite3
import csv
import setupDB

def login_tester(user, passw):
    print(setupDB.login(user, passw))



login_tester('wtf','wtf')
login_tester('jude','ASDASDAS')
login_tester('jason','zheng')

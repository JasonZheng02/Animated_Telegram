import sqlite3
import csv
import setupDB

def register_tester(user, pass1, pass2):
    print(setupDB.register(user, pass1, pass2))


register_tester('jason', 'zheng1', 'zheng2')
register_tester('jason', 'zheng', 'zheng')
register_tester('jude', 'rizzo', 'rizzo')
register_tester('manfred', 'tan123', 'tan123')
register_tester('asd', 'ads', 'ads')


#EXPECT:
# -1
# -1
# -3
# 2
# -1


# -2
# 3 SUCCESS
# -1
# 4 SUCCESS
# -3

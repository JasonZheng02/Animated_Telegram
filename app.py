# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Login():
    return render_template("login.html")

if __name__ == "__main__":
	app.debug = True
	app.run()

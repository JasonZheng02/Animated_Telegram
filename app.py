# Team Jacket
# SoftDev1 pd09
# P#01 ArRESTed Development
# 2019-11-??

from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Login():
    global lastRoute
    global loggedin
    loggedin = False
    lastRoute = "/"
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        c.execute("SELECT * FROM userdata")
        valid = c.fetchall()
        if("username" in session and "password" in session):
            if (session["username"], session["password"]) in valid:
                loggedin = True
                return redirect("/Main")
                #check if the credentials are in our userdatabase, if so they log in
    return rend_temp("LoginPage.html", message)

##check if the user entered a valid combo of username and passwor
@app.route("/loginHelper", methods=['GET', 'POST'])
def helper():
    global message
    global loggedin
    if (len(request.args) == 0): return redirect(lastRoute)
    with sqlite3.connect(DB_FILE) as db:
        c = db.cursor()
        c.execute("SELECT * FROM userdata")
        valid = c.fetchall()
        if (request.args["username"], request.args["password"]) in valid:
            session["username"] = request.args["username"]
            session["password"] = request.args["password"]
            loggedin = True
            return redirect("/Main")
        # if (session["username"], session["password"]) in valid:
        #     return redirect("/Main")
        message = "Username or password incorrect."
        return redirect("/")

@app.route("/Register", methods=['GET', 'POST'])
def Register():
    global lastRoute
    lastRoute = "/Register"
    return rend_temp("RegisterPage.html", message)

if __name__ == "__main__":
	app.debug = True
	app.run()

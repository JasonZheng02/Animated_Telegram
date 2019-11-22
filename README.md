# Animated_Telegram by Team Jacket

Roles
----------------------------------

#### Flask App Creator (Jude)
- Will create a Python flask application that will have each of the routes we need
- Will make sure that the user is logged in to pages that require it and not letting user go to random pages by typing in the URL
- Will make error messages
#### CSS (Jason)
- Will make the flask routes look nice
- Will make the playing cards look nice
#### Database Creator (Manfred)
- Will make a database to store information from the APIs
- Will make a database to store the decks made from the users
- Will make a database to store the users information

Description
----------------------------------
An online card game with similar ideas to Hearthstone.
Cards will be NHL players or pokemons

List of APIs:
----------------------------------
Deck of Cards API:
	No quota
	Used to shuffle decks, make decks, add to decks etc
  https://docs.google.com/document/d/1oCJhl-NoNNpekMLd4C4jBXhpL9xvm6ZrVIdfoqbq-Vc/edit
NHL API:
	No quota
	Stats on hockey players that will be converted into in game stats
  https://docs.google.com/document/d/1_CkEqysrBYJQ7XZBEWMpMrWhCQb0HPMPLGLknhnDtsA/edit
PokeAPI:
	Limit of 100 API requests per IP address per minute
	Stats on Pokemon that will be converted into in game stats
  https://docs.google.com/document/d/1hMbL36d5qqFLfufHOqUMWwraWFudfJdekqp6urex0KU/edit

How to Run
----------------------------------
**1)** Install Python3 and Flask if you have not done so already.
  - All your Flask-related needs:
  ```console
    $ pip3 install flask
  ```
**2)** Clone the repository and cd into it:
```console
  $ git clone git@github.com:CalfinChoo/blog.git
  ...
  $ cd blog
```
**3)** Run the following command:
```console
  $ python app.py
```
**4)** View the webpage in your browser at URL: http://127.0.0.1:5000/

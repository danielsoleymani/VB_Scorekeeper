from dotenv import load_dotenv
import os
from pymongo import MongoClient
from flask import Flask, request, render_template, redirect, session
from XConnect import X_Connect
from Game import Game
from Team import Team
from tweetFactory import Tweet_Factory

load_dotenv()

connection = os.getenv("DB_CONNECTION")
cluster = MongoClient(connection)
users = cluster.get_database("userDB").get_collection("users")

connection = X_Connect()

app = Flask(__name__)
app.secret_key = os.getenv("APP_KEY")

current_game = None

@app.route('/')
def start():
    return render_template('signin.html')  

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/signin", methods = ["POST"])
def signin():
    user = users.find_one({"email" : request.form.get("email"), "password" : request.form.get("password")})
    if user == None:
        return render_template("signin.html", error="Username or password is incorrect. Please try again.")
    elif user['twitter_token'] == None:
        return render_template('twitterConnect.html')
    else:
        session['user_email'] = user['email']
        return render_template("gamecreation.html")
  
@app.route("/signup/submit", methods = ["POST"])
def handle_signup():
    user = users.find_one({"email" : request.form.get("email")})
    if user == None:
        newUser = {"email": request.form.get("email"), "password" : request.form.get("password"), "name": request.form.get("name")}
        users.insert_one(newUser)
        session['user_email'] = request.form.get("email")
        return render_template('twitterConnect.html') 
    else:
        return render_template("signup.html", error="An account already exists under this email.")
    
@app.route("/xconnect")
def x_connection():
    url = connection.get_url()
    return redirect(url)

@app.route("/xverification", methods = ["GET"])
def x_verification():
    verifier = request.args.get("oauth_verifier")
    access_token, access_token_secret = connection.get_tokens(verifier)
    user_email = session.get("user_email")
    users.update_one({"email": user_email},{"$set": {"twitter_token": access_token, "twitter_secret": access_token_secret}})
    return render_template("gamecreation.html")


@app.route("/start", methods = ["POST"])
def startGame():
    global current_game
    user_email = session.get("user_email")
    team1_name = request.form.get("name1")
    team2_name = request.form.get("name2")
    team1_color = request.form.get("color1")
    team2_color = request.form.get("color2")
    number_of_sets = request.form.get("setNumbers")
    team1 = Team(team1_name, team1_color)
    team2 = Team(team2_name, team2_color)
    tf = Tweet_Factory(users.find_one({"email" : user_email})["twitter_token"], users.find_one({"email" : user_email})["twitter_secret"])
    current_game = Game(team1, team2, number_of_sets, tf)
    current_game.start_game()
    return render_template(
        "scoreboard.html", 
        team1_name=current_game.team1.name,
        team2_name=current_game.team2.name,
        team1_set_score=current_game.team1.set_score,
        team2_set_score=current_game.team2.set_score,
        team1_match_score=current_game.team1.match_score,
        team1_color=current_game.team1.primary_color,
        team2_color=current_game.team2.primary_color,
        team2_match_score=current_game.team2.match_score
    )

@app.route("/team1score")
def team1_score():
    current_game.team1.increase_score()
    if current_game.current_set.check_win()== None:
        end_game_condition = False
    else:
        end_game_condition = True

    return render_template(
        "scoreboard.html", 
        team1_name=current_game.team1.name,
        team2_name=current_game.team2.name,
        team1_set_score=current_game.team1.set_score,
        team2_set_score=current_game.team2.set_score,
        team1_match_score=current_game.team1.match_score,
        team2_match_score=current_game.team2.match_score,
        team1_color=current_game.team1.primary_color,
        team2_color=current_game.team2.primary_color,
        end_game_condition = end_game_condition
    )



@app.route("/team2score")
def team2_score():
    current_game.team2.increase_score()
    if current_game.current_set.check_win() == None:
        end_game_condition = False
    else:
        end_game_condition = True

    return render_template(
        "scoreboard.html", 
        team1_name= current_game.team1.name,
        team2_name= current_game.team2.name,
        team1_set_score= current_game.team1.set_score,
        team2_set_score= current_game.team2.set_score,
        team1_match_score= current_game.team1.match_score,
        team2_match_score= current_game.team2.match_score,
        team1_color=current_game.team1.primary_color,
        team2_color=current_game.team2.primary_color,
        end_game_condition = end_game_condition
    )

@app.route("/endSet")
def end_set():
    if current_game is not None or current_game.current_set is not None:
        if current_game.end_set(current_game.current_set.set_win()) == True:
            return render_template(
            "scoreboard.html", 
            team1_name= current_game.team1.name,
            team2_name= current_game.team2.name,
            team1_set_score= current_game.team1.set_score,
            team2_set_score= current_game.team2.set_score,
            team1_match_score= current_game.team1.match_score,
            team2_match_score= current_game.team2.match_score,
            team1_color=current_game.team1.primary_color,
            team2_color=current_game.team2.primary_color,
            end_game_condition = False
        )
        else:
            return render_template("twitterConnect.html")
    return


if __name__ == "__main__":
    app.run(debug=True)

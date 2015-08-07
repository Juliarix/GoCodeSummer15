'''
Golf Score Calculator App

The goal of this app is for you to be able to enter scores for different players and print a leaderboard.  You are given a file with the base scores for a default course that you will need to read in (ask an instructor if you don't understand golf!).

# Example UI in the Terminal:
# How many players are in the golf tournament? 2
# How many holes are in the golf course? 18
# What is the name for player 1? Jonathan Lau
# What is the name for player 2? Jeremy Schwartz
# What are the scores for player 1? [3,3,3,3,3...]
# What are the scores for player 2? [3,3,3,3,3]
# Type p to print the leaderboard: p
# LeaderBoard
# 1 - Jonathan Lau, Overall Score: 73, +1
# 2 - Jeremy Schwartz, Overall Score: 76, +5

You will implement this idea and create a golf score calculator using classes.  

You are free to adjust the gameplaym, how the app works, and to extend it as you wish.

Here are some basic recommendations for how to design your classes:

1) A CourseLayout class:

In charge of reading in the file with the base scores for the golf course.

You will use the file given to you as the default.  

Optionally, you can allow the user to enter a filename for a different golf course.

2) A PlayerScore class:

In charge of handling player information and scores

3) A AppInterface Class:

This has a simple method that runs the game and talks to the terminal I/O.

It also has a method that uses information from the CourseLayout and PlayerScore and prints a leaderboard.

Ex:

LeaderBoard
1 - Jonathan Lau, Overall Score: 73, +1
2 - Jeremy Schwartz, Overall Score: 76, +4

Note: The last number is simply the overall score minus 72 (it's how golf works...)

'''

# def CourseLayout():
#     with open (course_layout_1.txt, "r") as cl:
# 		par = cl.readlines()
#     for data in par:
#         par_course = sum(data)
#         print par_course
    # holes = raw_input("How many holes on this course?\n")

# def player_information():

     
def add_player(golf_hash):
        player_name = raw_input("What is your player's name?\n")
        player_array = []
        golf_hash[player_name] = player_array
        print golf_hash
        
def AppInterface():
    print "Welcome to All Eagles Golf Tracker"
    leaderboard = {}
    while True:
        command = raw_input("Please choose from the following list of commands.\n p - put a player on your scorecard.\n a - add scores to your scorecard\n l - list scores on leaderboard\n q - quits program\n")
        if command == "p":
            amt_players = 0
            try: 
                amt_players = int(raw_input("How many players in your tournament? Please choose a number 1-4.\n"))
            except:
                print "I said enter a number"
            if amt_players > 0 and amt_players <= 4:
                for num in range(amt_players):
                    add_player(leaderboard)
            else:
                print "Please choose a number 1-4."

        elif command == "a":
            hole_num = int(raw_input("Which hole do you want to enter a score for?\n"))
            if hole_num < 19:
                name = raw_input("Choose a player to enter a score for.\n")
                if leaderboard.has_key(name):
                    score = int(raw_input("What is your score for this hole?\n"))
                    score = leaderboard[name].append(score)
                    print score
            else:
                print "The 19th hole is at the clubhouse."
        elif command == "l":
            par = 72
            for each_score in leaderboard:
                if sum(leaderboard[each_score]) > par:
                    above_par = sum(leaderboard[each_score]) - par
                    print "Player:", each_score, "scored", sum(leaderboard[each_score]), ",", above_par, "above par"
                elif sum(leaderboard[each_score]) < par:
                    below_par = par - sum(leaderboard[each_score])
                    print "Player:", each_score, "scored", sum(leaderboard[each_score]), ",", below_par, "under par"

        elif command == "q":
            print "All Eagles Golf Tracker is now quitting."
            break
        else :
            print "That is not a valid command, please choose a command from the list."


    




print AppInterface()




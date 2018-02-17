import math
import random

"""
Pig Game

Instructions
============ 
2 players and goal is to reach a set number of points (20 pts)
- player one => roll dice, can choose to roll again or stop, if roll one you lose
- player two => roll dice, can choose to roll again or stop, if roll one you lose
- keep rolling until a person reaches 20

@author: anikaitsingh
"""

def main():
    greeting()
    playGame()
    goodbye()

def greeting():
    print "Welcome to the Pig Death Game"

def playGame():
    return

def rollDice():
    return random.randint(1,6)

def playerMove():
    total = 0
    again = "y"
    
    while(again == "y"):
        r = rollDice()
        if(r == 1):
            print "You rolled a 1. You lose"
            total = 0
            again = "y"
        else:
            total += r
            print "You rolled a {}. Your round score is {}".format(r,total)
            again = raw_input("Would you like to roll again (y/n)?:")
            
        print "Your turn is over with a round score of {}".format(total)
        return total

def computerMove():
    return        

def goodbye():
    print "Toodles"
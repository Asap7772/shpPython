import random
import math
###############################################################################
# SHP Computer Programming in Python (Accelerated)
# February 3rd,2018 
# Name: Anikait Singh
# Purpose: to play Mastermind Game
###############################################################################

def validConfig(s):
    if(len(s) != 4):
        return False
    
    x = [False,False,False,False,False,False] #represents a through F
    for a in s:
        a = str.upper(a)
        if(a == 'A'):
            if(x[0] == True):
                return False
            else:
                x[0] = True
        elif(a == 'B'):
            if(x[1] == True):
                return False
            else: 
                x[1] = True
        elif(a == 'C'):
            if(x[2] == True):
                return False
            else:
                x[2] = True
        elif(a == 'D'):
            if(x[3] == True):
                return False
            else:
                x[3] = True
        elif(a == 'E'):
            if(x[4] == True):
                return False
            else: 
                x[4] = True
        elif(a == 'F'):
            if(x[5] == True):
                return False
            else: 
                x[5] = True
        else: 
            return False
    return True


def contains(l, char):
    for x in l:
        if(str.lower(x) == str.lower(char)):
            return True
    return False

def guess(correct, config):
    if(correct == config):
        return [0, 0, 4] #array returned contains [none, white, black] pegs
    else:
        none = 0
        white = 0
        black = 0
        for i in range(0,len(config)):
            if(config[i] == correct[i]):
                black +=1
            elif(contains(correct, config[i])):
                white +=1
            else:
                none += 1
        return [none, white, black]
    
    
def num2Letter(i):
    if(i == 0):
        return 'A'
    elif(i == 1):
        return 'B'
    elif(i == 2):
        return 'C'
    elif(i == 3):
        return 'D'
    elif(i == 4):
        return 'E'
    else:
        return 'F'
    

def randConfig():
    x = ""
    while(len(x) != 4):
        char = num2Letter(int(random.random() * 6));
        if(not contains(x, char)):
            x += char
    return x
            
def run():
    computerConfig = randConfig()
    #print computerConfig
    
    print "Welcome to Mastermind";
    
    for i in range(12):
        inputStr = "Guess # {} Enter a 4 character configuration: ".format(i + 1)
        s = raw_input(inputStr) 
        won = False
        
        if validConfig(s):
            peg = guess(computerConfig, s)
            print "You have ", peg[1], " white pegs and ", peg[2], "black pegs."
            if(peg[2] == 4):
                won = True
                break
        else:
            print "Not a Valid Configuration. Please Try Again"
        
    if(won):
        print "Great Job. You won the Game!"
    else:
        print "Good try. Game Over! ", computerConfig, " was the correct configuration"
    
run();
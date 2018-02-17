###############################################################################
# SHP Computer Programming in Python (Accelerated)
# February 3rd,2018 
# Name: Anikait Singh:
# Purpose: to convert an english word to a pigLatin Word
###############################################################################


#method to determine whether a character is a vowel; not case sensitive
def isVowel(char):
    return (char == "a" or char == "e" or char == "i" or char == "o"
            or char == "u" or char == "A" or char == "E" or char == "I"
            or char == "O" or char == "U");

#returns first index of a vowel, if not found returns -1
def indexChar(s):
    for i in range(len(s)):
        if(isVowel(s[i])):
            return i
    return -1.

# method that converts english word to pig latin (using rules provided). 
# If vowel not found returns original string
def pigLatinize(s):
    i = indexChar(s)
    
    if(i == -1): 
        return s
    elif(i == 0):
        return s + "yay"
    else:
        return s[i:len(s)] + s[0:i] + "ay"

# loops and asks for user inpu
def run():
    s = raw_input("Please enter a word: ")
    while(s != "."):
        print s , " in pig latin is " , pigLatinize(s)
        print ""
        s = raw_input("Please enter another word: ")

#runs the program
run()
        
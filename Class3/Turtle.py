###############################################################################
# SHP Computer Programming in Python (Accelerated)
# Febrary 10, 2018
# Name: Anikait Singh
#
# File contains...
# e.g. file contains function to create a recursive tree pattern
###############################################################################

import turtle
from turtle import *

def branch(level):
    dot()
    branch_tree(100, level, 45 ,1.0/2)

def branch_tree(length, level,angle, ratio):
    if(level >= 1):
        left(angle)
        forward(length)
        right(angle)
        branch_tree(length*ratio, level-1, angle, ratio)
        left(angle)
        backward(length)
        right(2*angle)
        forward(length)
        left(angle)
        branch_tree(length*ratio, level-1, angle, ratio)
        right(angle)
        backward(length)
        left(angle)

#call to recursive function
def main():
    branch(3)

main()

done()# finish program main()

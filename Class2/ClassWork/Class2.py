import math
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:16:18 2018

@author: anikaitsingh
"""

a = 3

a = float(a)

b = 5

a/b

a//b

print math.pi #constant

print math.sqrt(5) #function called on parameter 5

print math.pow(2,5) #aka 2**5

print math.sin(math.pi/2)

import random

x = random.random() #exclusive between 1
x = random.randint(1,3) #inclusive

a = True
b = False

print a and b

a = "Bob"
b = "Jim"
print a[0: 2]

l = ["Happy", True, 5, 6.1]
print len(l)

a = True
b = False

if(a):
    print "bob"

name = raw_input("Hello, What is your name: ")

print "Hello " + name

age = raw_input("How old are you: ")

computerAge = 15
print "You are {} years older than me".format(int(age)-computerAge)
print "You are ",int(age)-computerAge, " years older than me" # alternate way
print "I want {} scoops of ice cream, {} chocolate bars, and {} muffins".format(3,5,4)
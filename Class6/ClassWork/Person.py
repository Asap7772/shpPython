#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:09:21 2018

@author: anikaitsingh
"""

class Person(object):
    
    def __init__(self, first = '', last = '', age = 0):
        self.firstname = first
        self.lastname = last
        self.age
    
    def __str__(self):
        return "{} {}, {}".format(self.firstname, self.lastname, self.age)
    
    def __cmp__(self, other):
        return cmp(self.lastname, other.lastname)
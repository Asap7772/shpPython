#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:12:50 2018

@author: anikaitsingh
"""

from Person import Person

class Student(Person):
    
    def __init__(self, first = '', last = '', age = 0, number = 0):
        super(Student,self).__init(first, last, age)
        self.id = number
    
    def __str__(self):
        return super(Student, self).__str__() + "," + str(self.id)
    
    def __cmp__(self, other):
        return super(Student, self).__cmp__(other)
    
    
bob = Student('kelly', 'ryu', 20, 2362)
fred = Student('kelly', 'smith', 20, 2362)

print bob>fred
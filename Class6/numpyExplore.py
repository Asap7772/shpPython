#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:23:20 2018

@author: anikaitsingh
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(10, 10)
a = a < 0.7
plt.matshow(a)
plt.show()

fig = plt.figure()
gr1 = fig.add_subplot(121)
gr2 = fig.add_subplot(122)

var1 = np.linspace(0,3,50)
var2 = var1 ** 2


gr1.plot(var1, var2, "o")
gr1.set_title('x^2 vs x')
gr1.set_xlabel('x')
gr1.set_xlabel('x^2')

gr2.plot(var2, var1,  "o")
gr2.set_title('root x vs x')
gr2.set_xlabel('x')
gr2.set_xlabel('root x')
plt.show()

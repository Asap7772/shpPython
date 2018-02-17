import circle as c # can shorten name
"""
Created on Sat Feb 10 10:05:12 2018

@author: anikaitsingh
"""

def f(a, b, **c):
    print a, b, c
    print c.get('bob')
    print c.keys()
    print c.values()


def fib(x):
    if(x <2):
        return 1
    else:
        return fib(x-2) + fib(x-1)

def reverseString(a):
    if(len(a) == 1):
        return a
    else:
        last = len(a) - 1
        return a[last] + reverseString(a[0:last])

def main():
    radius = 4
    print c.area(radius)
    f("Fall", "Winter", Sprint = "Verizon", Gym = 12, x = 8957, bob = True)
    print fib(10)
    print reverseString("palindrome")

main()    
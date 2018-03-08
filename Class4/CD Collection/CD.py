###############################################################################
# SHP Computer Programming in Python (Accelerated)
# Febrary 17th, 2018
# Anikait Singh :
# File contains... CD Class
###############################################################################

class CD():
    def __init__(self, title = "", artist = "", cost = 0, trackNum = 0):
        self.title = title
        self.artist = artist
        self.cost = cost
        self.trackNum = trackNum

    def __str__(self):
        return "{} by {} costs ${} and has {} tracks".\
        format(self.title,self.artist,self.cost,self.trackNum)

    def __cmp__(self, other):
        return cmp(self.title, other.title)

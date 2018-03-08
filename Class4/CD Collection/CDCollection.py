from CD import CD
###############################################################################
# SHP Computer Programming in Python (Accelerated)
# Febrary 17th, 2018
# Anikait Singh :
# File contains... CD Collection Class
###############################################################################

class CDCollection():

    def __init__(self):
        self.cds = []
        self.count = 0
        self.totalCost = 0

    def addCD(self, title, artist, cost, tracks):
        cd = CD(title,artist,cost,tracks);
        self.count = self.count + 1
        self.totalCost = self.totalCost + cost
        self.cds.append(cd)

    #method used to swap indices
    def swapCD(self, i, j):
        x = self.cds[i]
        self.cds[i] = self.cds[j]
        self.cds[j] = x

    #used bubble sort
    def sortCD(self):
        c = -1 #assume unsorted when begin
        while(c != 0):
            c = 0; #reset after swaps are done
            length = len(self.cds)
            for i in range(1, length):
                if(cmp(self.cds[i], self.cds[i-1]) <1):
                    self.swapCD(i, i-1);
                    c+=1;


    def removeCD(self, title):
        length = len(self.cds)
        for i in range(1, length):
            if(self.cds[i].title == title):
                cd = self.cds[i]
                self.count -= 1
                self.totalCost -= cd.cost
                self.cds.remove(cd)
                return;

    def __str__(self):
        string = "You have {} cds with a total cost of ${}: ".\
            format(self.count, self.totalCost)
        length = len(self.cds)
        for i in range(0, length):
            string = string + "\nCD # {} is the ".format(i+1) + str(self.cds[i])
        return string + "\n";

from Color import Color;
import numpy as np;

class Image():
    colorSize = 0;
    collumns = 0; 
    rows = 0;
    data = [];

    def __init__(self, fileName):
        f = open(fileName,'r');
        x = f.readline().strip();
        if('P3' != x):
            print('Exception');
        
        x = f.readline().strip();
        dimensions = x.split(' ');
        self.collumns = int(dimensions[0]);
        self.rows = int(dimensions[1]);
        self.colorSize = int(f.readline().strip());
        
        print self.collumns
        print self.rows
        print self.colorSize
        print ""
        
        self.data = [[Color()] * self.collumns] * self.rows;
        
        self.data = np.array(self.data)
        print np.shape(self.data)
        
        for i in range(self.rows):
            x = f.readline().strip().split(' ');
            for j in range(self.collumns):
                self.data[i][j] = Color(int(x[j*3]), int(x[j*3 + 1]), int(x[j*3 + 2]));
    
    def setColor(self, i =0, j = 0 , c = Color()):
        self.data[i][j] = c;
    
    def getColor(self, i =0, j = 0):
        return self.data[i][j];
    
    def export(self, fileName = "a.ppm"):
        var = open(fileName, 'w');
        var.write("P3\n");
        var.write(str(self.collumns) + " " + str(self.rows) + "\n");
        var.write(str(self.colorSize) + "\n");
        print "writing to file"
        var.write(self.__str__())
        var.close();
        
    def __str__(self):
        string = "";
        for i in range(self.rows):
             for j in range(self.collumns):
                 string = string + " " + self.getColor(i,j).__str__();
             string += "\n";
        return string;
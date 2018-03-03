from Image import Image;

class Effects():
    
    def run(self):
        self.x = Image("pictures/small.ppm");
        print ""
        self.grayscale()
    
    def grayscale(self):
        for i in range(self.x.rows):
            for j in range(self.x.collumns):
                 c = self.x.getColor(i,j)
                 average = (c.r + c.g + c.b)/3;
                 c.r = average;
                 c.g = average;
                 c.b = average;
        self.x.export("pictures/grayscale.ppm")
        
    def vLines(self):
        for i in range(self.x.rows):
            for j in range(0, self.x.collumns, 2):
                c = self.x.getColor(i,j)
                c.r = 255
                c.g = 255
                c.b = 255
        self.x.export("pictures/verticalLines.ppm")
        
    def negateRed(self):
        for i in range(self.x.rows):
            for j in range(0, self.x.collumns):
                c = self.x.getColor(i,j)
                c.r = self.x.colorSize - c.r
        self.x.export("pictures/negateRed.ppm")
        
    def negateBlue(self):
        for i in range(self.x.rows):
            for j in range(0, self.x.collumns):
                c = self.x.getColor(i,j)
                c.b = self.x.colorSize - c.b
        self.x.export("pictures/negateBlue.ppm")
           
    def negateGreen(self):
        for i in range(self.x.rows):
            for j in range(0, self.x.collumns):
                c = self.x.getColor(i,j)
                c.g = self.x.colorSize - c.g
        self.x.export("pictures/negateGreen.ppm")
        
    def negative(self):
        for i in range(self.x.rows):
            for j in range(0, self.x.collumns):
                c = self.x.getColor(i,j)
                c.r = self.x.colorSize - c.r
                c.b = self.x.colorSize - c.b
                c.g = self.x.colorSize - c.g
        self.x.export("pictures/negative.ppm")
    
    def mirror(self):
        for i in range(self.x.rows):
            for j in range(self.x.collumns/2):
                c = self.x.getColor(i,j);
                self.x.setColor(i, j, self.x.getColor(i,self.x.collumns-j-1))
                self.x.setColor(i, self.x.collumns-j-1,c)
        self.x.export("pictures/mirror.ppm")
    
c = Effects()
c.run();
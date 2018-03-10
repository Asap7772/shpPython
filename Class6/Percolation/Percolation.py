import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
np.set_printoptions(threshold=np.inf);

class Percolation(object):
    
    def __init__(self, n = 1, p = 0.5):
        self.n = n;
        self.p = p;
        self.a = np.random.rand(n, n)
        self.a = self.a > p
        self.a = self.a.astype(int)
        
        print self.a;
        
        self.show()
        
    def __str__(self):
        return 'size: {} x {}\nProbability:{}'.format(self.n , self.n , self.p)
    
    def show_flow(self):
        for j in range(self.n):
            if(self.a[0,j] == 0):
                self.flow(0,j);
        self.show()
    
    # I is collumn, j is row
    def flow(self, i, j):
        self.a[i][j] = 2;
        
        if(i-1 >= 0 and self.a[i-1,j] == 0):
            self.flow(i-1, j);
        
        if(i+1 < self.n and self.a[i+1,j] == 0):
            self.flow(i+1, j);

        if(j-1 >= 0 and self.a[i, j-1] == 0):
            self.flow(i, j-1);
        
        if(j+1 < self.n and self.a[i, j+1] == 0):
            self.flow(i, j+1);

    def show(self):
        c = mpl.colors.ListedColormap(['white', 'black', 'blue'])
        n = mpl.colors.Normalize(vmin=0,vmax=2)
        plt.matshow(self.a, cmap=c, norm=n)
        plt.show()

    def percolates(self):
        self.show_flow()
        for i in range(self.n):
            if(self.a[self.n-1,i] == 2):
                return True;
        return False;
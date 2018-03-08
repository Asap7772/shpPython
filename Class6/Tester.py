from Percolation import Percolation

def run():
    n = int(raw_input('Size of the Matrix: '));
    p = float(raw_input('Site vacancy probability: '))

    perc = Percolation(n, p)
    
    print 'Percolation occurs: {}'.format(perc.percolates())
    
    
run();
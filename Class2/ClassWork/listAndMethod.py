def addone(v):
    return v+1;

def add(a,b):
    return a+b;

v = 1;

print add(v, addone(v));

print;

l = [1,2,3]

for i in range(len(l)):
    print l[i]
    
    
print;
print l.count(3)

l.append(3)

print l
print l.count(3)
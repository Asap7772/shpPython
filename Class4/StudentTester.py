from Student import Student

s1 = Student("Anikait", "Singh", 5142) #do not need to specify self (placeholder)
print s1

s2 = Student("Indiana", "Jones") #because of keyword arguments
print s2

print "\nUsed Update Method"
print "=================="
s2.update("", "", 592)
print s2


print "\nAccessing Variables"
print "==================="
print "Name = ", s1.firstName
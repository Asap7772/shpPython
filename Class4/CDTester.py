from CDCollection import CDCollection

###############################################################################
# SHP Computer Programming in Python (Accelerated)
# Febrary 17th, 2018
# Anikait Singh :
# File contains... CD Collection Class
###############################################################################

x = CDCollection()

print x

x.addCD("Christmas Playbook", "Santa Claus", 3.00, 25)
x.addCD("Pop Hits", "Ed Sheeran", 1.50 , 15)
x.addCD("Rap Delights", "Eminem ", 1.50 , 15)
x.addCD("EDM", "Marshmello", 1.50 , 15)
x.addCD("Classical", "Beethoven", 1.50 , 15)
print x

x.sortCD()
print x

x.removeCD("Rap Delights")
print x
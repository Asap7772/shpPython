#########################################
# Representation of Standard Playing Card
# Attributes
# ==========
# suit = (0-3)
# rank = (0-12)
#########################################

class Card():
	
	suit_names = {"Clubs", "Diamonds", "Hearts", "Spades"}
	rank_names = {"Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}

	#Constructor
	def __init__(self, suit = 0, rank = 0):
		self.suit = suit
		self.rank = rank

	#To String Method
	def __str__(self):
		print "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

	# Compare Method
	# returns 1 if self > other
	# returns -1 if self < other
	# returns 0 if self = other
	
	def __cmp__(self, c):
		t1 = [self.rank, self.suit]
		t2 = [self.rank, self.suit]
		return __cmp__(t1, t2)

	# Alternate Solution
	#	def __cmp__(self, c = Card()):
	#		if(self.rank > c.rank):
	#			return 1
	#		elif(self.rank < c.rank):
	#			return -1
	#		else 
	#			return cmp(self.suit, other.suit)




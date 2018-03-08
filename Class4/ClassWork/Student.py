class Student():
	
	#Keyword Arguments for setting default value
	def __init__(self, first = "", last = "", id = 0):
		self.firstName = first
		self.lastName = last
		self.idNum = id

	# Need self as parameter
	def update(self, first = "", last = "", id = 0):
		#if first means is string not empty
		if first:
			self.firstName = first
		if first:
			self.lastName = last
		if id:
			self.idNum = id

	def __str__(self):
		return "{} {}, ID #: {}".format(self.firstName, self.lastName, self.idNum)


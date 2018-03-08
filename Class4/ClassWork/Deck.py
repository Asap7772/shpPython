from Card import Card
import random

class Deck():

	def __init__(self):
		self.current = []
		for i in range (0,4):
			for j in range(0,12):
				self.current.append(Card(i,j))

	def __str__(self):
		return str(len (self.current))

	def deal(self):
		card1 = self.current.pop()
		return card1

	def shuffle(self):
		random.shuffle(self.current)


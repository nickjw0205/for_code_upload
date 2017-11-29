import random

class Card:
	"""defines Card class"""
	__suits = ("Diamond","Heart","Spade","Clover")
	__ranks = ("Ace","1","2","3","4","5","7","8","9","10","J","Q","K")

	@staticmethod 
	def fresh_deck(): 
		cards = []          
		for s in Card.__suits:              
			for r in Card.__ranks:                  
				cards.append(Card(s,r,False))          
		random.shuffle(cards)          
		return cards
	def __init__(self, suit, rank, face_up = False):
		"""initializes a playing card object 
        arguments: 
        suit -- must be in suits 
        rank -- must be in ranks          
        face_up -- True or False (defaut True) 
        """ 
		self.__suit = suit
		self.__rank = rank    
		self.__face_up = face_up

	def __str__(self):
		"""returns its string representation"""
		if self.__face_up == True:
			return self.__suit + "." + self.__rank
		else:
			return "XXXX"

	def filp(self):
		"""flips itself""" 
		self.__face_up = not self.__face_up
	@property
	def suit(self):
		"""returns its suit value"""
		return self.__suit
	@property	
	def rank(self):
		"""returns its rank value"""  
		return self.__rank
	@property	
	def face_up(self):
		"""returns its face_up value"""
		return self.__face_up




			
"""
General schema 
to determine if a string is in the language:

way to do it 
start scanning from the left end
go over the string one symbol at a time
reach the end to be ready for the answer
"""

"""
plan 

define a class and initialize it with nothing having three attributes:
startState, currentState and prevState. 
the class will have isIn function that takes in a string to see if it is 
in the language, set of all even zeroed binary strings. 
"""

class Even_lang_checker():

	def __init__(self):
		self.startState = True
		self.currentState = True
		self.prevState = True

	def isIn(self, string):
		if set(list(string)) != {"1","0"}:
			return False
		else:
			for letter in string:
				if letter != 0:
					self.currentState = self.prevState
				else:
					self.currentState = not self.prevState
			if self.currentState:
				return True
			else:
				return False

checker = Even_lang_checker()
print(checker.isIn("01010101010100101100"))
print(checker.isIn("0000000000000000"))
print(checker.isIn("11111111111"))
print(set(list("010010010100101010001")))

class Player(object):

# Attributes of Mafia player: username, alignment and role
	
	def __init__(self, name, align, role):
		self.name = name
		self.alignment = align
		self.role = role
	
	def setPlayerName(self, name):
		self.name = name
		
	def setAlignment(self, align):
		self.alignment = align
		
	def setRole(self, role):
		self.role = role
	
	def getPlayerName(self):
		return self.name
	
	def getPlayerAlign(self):
		return self.alignment
		
	def getPlayerRole(self):
		return self.role

# Add player function
def addPlayer(name, align, role):
	player = Player(name, align, role)
	return player
	
#test = addPlayer("Zexy", "Mafia", "Godfather")
#print("This player's name is %s aligned with %s and with role %s" % (test.getPlayerName(), 
#	test.getPlayerAlign(), test.getPlayerRole()))
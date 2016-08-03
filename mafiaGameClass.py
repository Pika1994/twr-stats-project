class mafiaGameClass():
	
	def __init__(self):
	# This initializes all the properties that one may see in a Mafia game
		self.numofTown = 0 # int
		self.numofMafia = 0 # int
		self.numofInd = 0 # int
		self.currPhase = 0 # int
		self.host = [] # This and everything constructor below is a list
		self.winSide = []
		self.townPlayers = []
		self.mafiaPlayers = []
		self.indepPlayers = []
		self.deadTown = []
		self.deadMafia = []
		self.deadIndep = []

	# The add___ functions puts players in their respective sides in a list and counts each player
	# of that side 
	
	def addTownPlayer(self, townie):
		self.townPlayers.append(townie)
		self.numofTown += 1
	
	def addMafiaPlayer(self, scum):
		self.mafiaPlayers.append(scum)
		self.numofMafia +=1
		
	def addIndPlayer(self, ind):
		self.indepPlayers.append(ind)
		self.numofInd += 1
	
	# The curr___count functions returns the current count of the respective sides as an int
	
	def currTownCount(self):
		return self.numofTown
		
	def currMafiaCount(self):
		return self.numofMafia
		
	def currIndCount(self):
		return self.numofInd
		
	# The curr___list functions returns the current players that are alive in their respective sides
	# as a list
	
	def currTownList(self):
		return self.townPlayers
	
	def currMafiaList(self):
		return self.mafiaPlayers
	
	def currIndList(self):
		return self.indepPlayers
		
	# The getdead___ functions returns the dead players in their respective sides as a list
		
	def getDeadTown(self):
		return self.deadTown
	
	def getDeadMafia(self):
		return self.deadMafia
	
	def getDeadInd(self):
		return self.deadIndep
		
	# The remove___ functions removes the player from that list and puts them in the dead list 
	# in their respective sides
	
	def removeTown(self, town):
		self.townPlayers.remove(town)
		self.deadTown.append(town)
		self.numofTown -= 1 
	
	def removeMafia(self, scum):
		self.mafiaPlayers.remove(scum)
		self.deadMafia.append(scum)
		self.numofMafia -= 1	
			
	def removeInd(self, ind):
		self.indepPlayers.remove(ind)
		self.deadIndep.append(ind)
		self.numofInd -= 1
	
	# The nextPhase function increments the current phase by 1
	
	def nextPhase(self):
		self.currPhase += 1
	
	# The getCurrPhase function returns the current phase
	
	def getCurrPhase(self):
		return self.currPhase
	
	# The setHost function sets the host of the game
	
	def setHost(self, host):
		self.host.append(host)
	
	# The getHosts function returns the current hosts as a list
	
	def getHosts(self):
		return self.host
	
	# The setVictor function puts the winners of the game in a list
	
	def setVictor(self, faction):
		self.winSide.append(faction)
	
	# The getVictor function returns the winners of the game as a list
	
	def getVictor(self):
		return self.winSide
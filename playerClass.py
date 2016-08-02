class Player(object):
	name = ""
	postCount = 1
	alignment = ""
	
# Attributes of Mafia player: username, postcount in-thread and the alignment
	
	def __init__(self, name, alignment, postCount=1):
		self.name = name
		self.postCount = postCount
		self.alignment = alignment

def addPlayer(name, align):
	player = Player()
	player.name = name
	player.alignment = align
	return player

'''	
# DEBUG STATEMENT

username = input("Enter a username: ")
align = input("Enter an alignment: ")

player1 = Player(username, align)

print("The alignment of %s is %s and posted %d times" % (player1.name, player1.alignment, player1.
	postCount))

EXPECTED OUTPUT: "The alignment of USERNAME is ALIGN and posted 1 times"

'''
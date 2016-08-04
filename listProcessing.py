from mafiaGameClass import mafiaGameClass as Game
from playerClass import playerClass as Player
from sys import argv

if len(argv) != 2:
	exit("Usage: python csv input")
	
playerList = argv[1]


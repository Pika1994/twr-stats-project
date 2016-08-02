from playerClass import Player
from sys import argv
import csv

if(len(argv) != 2):
	exit("Usage: python Postcount playerlist")

playerList = open(argv[1])
playerList = csv.reader(playerList)
playerList = list(playerList)

for player in range(len(playerList)):
	players = Player(playerList[player][0], playerList[player][1])
	print("%s is aligned with %s" % (players.name, players.alignment))
	

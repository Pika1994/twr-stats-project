from mafiaGameClass import mafiaGameClass as Game
import playerClass as Player
from sys import argv
import csv

if len(argv) != 2:
	exit("Usage: python csv input")
	
playerList = open(argv[1])
playerList = csv.reader(playerList)

game = Game()
# p = Player()
players = []

for player in playerList:
   p = Player.addPlayer(player[0], player[1], player[2])
   print("%r is %r with role %r" %(p.getPlayerName(), p.getPlayerAlign(), p.getPlayerRole()))
 #  print(p.getPlayerAlign())
   if p.getPlayerAlign() == "Town":
        game.addTownPlayer(player[0])
   elif p.getPlayerAlign() == "Mafia":
        game.addMafiaPlayer(player[0])
   else:
        game.addIndepPlayer(player[0])

# TO-DO: Need to implement an output to .csv file now to prepare for the visualization
        
'''print("There are %d town players and %d Mafia players" % (game.currTownCount(), game.currMafiaCount()))
print(game.currTownList())  
print(game.currMafiaList())'''
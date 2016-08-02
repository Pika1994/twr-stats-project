from playerClass import Player

# while True:
username = input("Enter a username: ")
align = input("Enter an alignment: ")
player1 = Player(username, align)

print("The alignment of %s is %s and posted %d times" % (player1.name, player1.alignment, player1.
postCount))
	
player1.postCount += 1
player1.postCount += 1
	
print("The alignment of %s is %s and posted %d times" % (player1.name, player1.alignment, player1.
	postCount))
	
'''	again = input("Do you want to continue? y/n ")
	if again == "n":
		exit()
'''
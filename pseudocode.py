#Game is based off of a 2 dimensional grid movement. The grid is created by:

#yaxis0 = . . . . .
#yaxis1 = . . . . .
#yaxis2 = D . X . .
#yaxis3 = . . . . .
#yaxis4 = . . . . .

#The different characters on the graph represent different tile types
#the grid's x is the player (subject to change), which denotes most functions
#the grid is accessed by the player through the w a s d keys
#activeyaxis = yaxis with the player
#xaxis = position in the yaxis list
#after every movement the map will be redrawn
#the map will also have "events" on it
#when the player "collides" with these events, a unique set of code is run
#the door in the example (D), draws a new map.

#the game will include fighting
#the fighting system an enemy image drawn similarily to the map
#the player will have access to a set of moves that are acquired and listed

#moves = slash, block, parry

#the fighting will also include a bag which includes items
#these items can be used, consuming them and deleting them
#example items would be a healing salve or a bomb

#the fighting system will not be the main focus

#the main focus of this game will be to simulate an economy
#this will be done through a series of formulas
#the map will denote "towns"
#each of these towns has a series of values, ranging from population to tools
#each of these values will change based on the amount of time passed
#the time passed will be represented by console inputs
#using rng and supply and demand, the value of items within the towns will vary
#the players goal is to amass wealth
#this is done by abusing the difference in town item values.
#each item will have a minimum of 2 values linked to it:
#number of the item owned, as well as value of the given items
#the value is determined through rng, aswell as the difference in core value
#between the item and the other items that are linked to it
#an example would be:

#population = 500
#food = 730
#foodvalue = 5
#if (food >= population):
#   foodvalue = foodvalue * (.8, 1)
#if (food <= population):
#   foodvalue = foodvalue * (1, 1.2)

#The item values will be dynamic, however, being produced asymetrically
#The game will be a sort of "high score" game, where the player will try to
#amass a substantial amount of wealth by a specific interval, or by the time
#they die.

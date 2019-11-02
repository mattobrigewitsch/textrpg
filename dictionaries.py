#Matt Obrigewitsch
#CS 30
#October 22nd
#Uses dictionaries to outline the key locations, character, and inventory

print("please print your name")
charname = input()  # Sets the characters name, accessed in Character
skillname = "skill name"  # A placeholder for character
character = {
    'name': charname,
    'skill': skillname}

#Inventory is a nested dictionary for everything the player has collected.
#It Each item has a description, value and amount, and can be sold at villages.
inventory = {'food': {'value': 2, 'description': 'an essential for survival'
             , 'amount': 5},
             'luxury goods': {'value': 25, 'description': 'high value fancy goods',
             'amount': 1}}

#Location is used later to check if the world map is open, which is navigaed
#with W A S D, on a displayed grid. Rorikstead and Oberperfuss are the names
#of the two villages.
location = {
        'world map': True,
        'rorikstead': False,
        'oberperfuss': False}

print("your name is " + character['name'])
print("you skill is " + character['skill'])

print("")

print("Food: " + inventory['food']['description'])
print("you have " + str(inventory['food']['amount']) + " units of food")
print("each unit is worth " + str(inventory['food']['value']))

print("")

print("Luxury Goods: " + inventory['luxury goods']['description'])
print("you have " + str(inventory['luxury goods']['amount']) + " units of luxury goods")
print("each unit is worth " + str(inventory['luxury goods']['value']))

print("")

if location['world map']:
    print("the world map is open")
else:
    print("the world map is not open")

if location['rorikstead']:
    print("you are in Rorikstead")
else:
    print("you are not in Rorikstead")

if location['oberperfuss']:
    print("you are in Oberperfuss")
else:
    print("you are not in Oberperfuss")

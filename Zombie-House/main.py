#!/bin/python3

'''
Remix from original project published by Raspberry Pi Foundation 
https://projects.raspberrypi.org/en/projects/rpg
Integrated code from https://github.com/xAptive
Converted code to use f-strings (available in Python 3.6 and newer)
'''

# NOTE: This code is in the 'working' branch

def showInstructions():
  # print a main menu and the commands
  print('''
*********************
* Zombie House Game *
*********************

Objectives:
Get to the Garden and escape with a key and potion
Defend yourself against the Zombies with a sword
Protect yourself against the Poisons with a potion

Commands:
  go [direction] (Options -> north, south, east or west)
  get [item] (Options -> key, sword or potion)
  exit (Exit the game)
  
''')

def showStatus():
  # print the player's current status
  print('---------------------------')
  print(f"You are in the {currentRoom}")
  # print the current inventory
  print(f"Inventory : {str(inventory)}")
  # print the available directions
  for direction in rooms[currentRoom]['directions']:
    print(f"The {rooms[currentRoom]['directions'][direction]} is {direction}")
  # print an item, monster or poison if there is one
  if "item" in rooms[currentRoom]:
    print(f"You see a {rooms[currentRoom]['item']}")
  if "monster" in rooms[currentRoom]:
    print(f"There is a {rooms[currentRoom]['monster']} in the room!")
  if "poison" in rooms[currentRoom]:
    print(f"There is some {rooms[currentRoom]['poison']} in the room!")
  print("---------------------------")

# An inventory, which is initially empty
inventory = []

'''
A dictionary is used to link a room to other rooms and
define what is contained inside the room.
The directions a player can move are in a nested dictionary.
Rooms can contain an item, monster or poison
An item is something the player can use (protect/defend)
whereas a monster or poison are non-playable (NPC), but can 
do damage to a player
'''
rooms = {

            'Hall' : {
              'directions' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'north' : 'Atrium',
                  'west' : 'Library'
              },
              'item' : 'key'
            },

            'Kitchen' : {
              'directions' : {
                  'north' : 'Hall',
                  'east' : 'Pantry'
              },
              'monster' : 'Zombie',
              'item' : 'flower'
            },
            
            'Dining Room' : {
              'directions' : {
                  'west' : 'Hall',
                  'south' : 'Pantry',
                  'north' : 'Bedroom'
              },
              'item' : 'sword'
            },
            
            'Atrium' : {
              'directions' : {
                  'south' : 'Hall',
                  'west' : 'Parlor',
                  'east' : 'Bedroom',
                  'north' : 'Garden'
              }
            },
            
            'Library' : {
              'directions' : {
                  'east' : 'Hall',
                  'south' : 'Study',
                  'north' : 'Parlor'
              },
              'item' : 'potion'
            },
            
            'Study' : {
              'directions' : {
                  'north' : 'Library'
              },
              'poison' : 'hemlock'
            },
            
            'Parlor' : {
              'directions' : {
                'south' : 'Library',
                'east' : 'Atrium'
              },
              'monster' : 'Zombie'
            },
            
            'Pantry' : {
              'directions' : {
                'west' : 'Kitchen',
                'north' : 'Dining Room'
              },
              'monster' : 'Zombie'
            },
            
            'Bedroom' : {
              'directions' : {
                'south' : 'Dining Room',
                'west' : 'Atrium'
              },
              'poison' : 'hemlock'
            },
            
            'Garden' : {
              'directions' : {
                'south' : 'Atrium'
              }   
            }

         }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
  try:
    
    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':  
      move = input('>')
    
    move = move.lower().split()

    # if they type 'go' first
    if move[0] == 'go':
     # check that they are allowed wherever they want to go
      if move[1] in rooms[currentRoom]['directions']:
        # set the current room to the new room
        currentRoom = rooms[currentRoom]['directions'][move[1]]
      # there is no door (link) to the new room
      else:
          print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get' :
      # if the room contains an item, and the item is the one they want to get
      if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        # add the item to their inventory
        inventory += [move[1]]
        # display a helpful message
        print(move[1] + ' picked up!')
        # delete the item from the room
        del rooms[currentRoom]['item']
      # otherwise, if the item isn't there to get
      else:
        # tell player they can't get it
        print('Can\'t get ' + move[1] + '!')
         
    # Allow command to exit the game
    if move[0] == 'exit':
      break
      
    # Player loses game if they enter room with Zombie without a Sword
    if 'monster' in rooms[currentRoom] and 'Zombie' in rooms[currentRoom]['monster'] and 'sword' in inventory:
      print('You have defended yourself from the Zombie attack! ... Continue On')
    elif 'monster' in rooms[currentRoom] and 'Zombie' in rooms[currentRoom]['monster']:
      print('A Zombie has eaten your brainz. You need to defend yourself ... GAME OVER!!!')
      break
  
    # Player loses game if they enter room with poison without a potion
    if 'poison' in rooms[currentRoom] and 'hemlock' in rooms[currentRoom]['poison'] and 'potion' in inventory:
      print('The potion has protected you from the Poison! ... Continue On')
    elif 'poison' in rooms[currentRoom] and 'hemlock' in rooms[currentRoom]['poison']:
      print('The Poison Hemlock has killed you. A potion will protect you ... GAME OVER!!!')
      break
  
    # Player wins game if they get to the Garden with the key and magic potion
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
      print('You have escaped the house with the Key and Magic Potion ... YOU WIN!!!')
      break
    elif currentRoom == 'Garden':
      print('To escape you need the key and potion ... Keep Looking')
      
  except KeyboardInterrupt:
    break
#!/bin/python3

'''
Remix from original project published by Raspberry Pi Foundation
https://projects.raspberrypi.org/en/projects/rpg
Integrated code from https://github.com/xAptive
MIT License - Copyright (c) 2019 Dave Tucker
Converted code to use f-strings (available in Python 3.6 and newer)
'''

# NOTE: This code is in the 'master' branch

from map import *

def showInstructions():
  """Print a main menu and the commands"""

  print('''
*********************
* Zombie House Game *
*********************

Objectives:
Get to the Garden and escape with a key and potion
Defend yourself against the Zombies with a sword
Protect yourself against the Poisons with a potion
If you find a map, you can see the map using the command 'show map'

Commands:
  go [direction]
  get [item]
  show map
  exit

''')

def showStatus():
  """Print the player's current status"""

  print("---------------------------")
  print(f"You are in the {currentRoom}")
  # print the room description, if given
  if "description" in rooms[currentRoom]:
    print(f"{rooms[currentRoom]['description']}")
  # print your health score
  print(f"Health : {health}")
  # print the current inventory
  print(f"Inventory : {str(inventory)}")
  # print the available directions
  for direction in rooms[currentRoom]['directions']:
    print(f"The {rooms[currentRoom]['directions'][direction]} is {direction}")
  # print an item, monster or poison if there is one
  if "item" in rooms[currentRoom]:
    print(f"You see a {rooms[currentRoom]['item']}")
    if "item description" in rooms[currentRoom]:
        print(rooms[currentRoom]["item description"])
  if "monster" in rooms[currentRoom]:
    print(f"There is a {rooms[currentRoom]['monster']} in the room!")
  if "poison" in rooms[currentRoom]:
    print(f"There is some poison {rooms[currentRoom]['poison']} in the room!")
  print("---------------------------")


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
              'description' : 'The main downstairs hallway. \nYou see more rooms in every direction.'
            },

            'Kitchen' : {
              'directions' : {
                  'north' : 'Hall',
                  'east' : 'Pantry'
              },
              'monster' : 'Yellow Zombie',
              'item' : 'flower',
              'description' : 'A large, very clean kitchen. \nWhy is that flower here?'
            },

            'Dining Room' : {
              'directions' : {
                  'west' : 'Hall',
                  'south' : 'Pantry',
                  'north' : 'Guest Bedroom'
              },
              'item' : 'sword',
              'description' : 'A grand dining room. There is a long, majestic \nmahagony table in the center of the room'
            },

            'Atrium' : {
              'directions' : {
                  'south' : 'Hall',
                  'west' : 'Parlor',
                  'east' : 'Guest Bedroom',
                  'north' : 'Garden',
                  'up' : 'Upstairs Hall'
              },
              'description' : 'An atrium with a high, vaulted ceiling. \nThere are stairs leading up.'
            },

            'Library' : {
              'directions' : {
                  'east' : 'Hall',
                  'south' : 'Study',
                  'north' : 'Parlor'
              },
              'item' : 'potion',
              'description' : 'An impressive collection of very old books.'

            },

            'Study' : {
              'directions' : {
                  'north' : 'Library'
              },
              'poison' : 'hemlock',
              'item' : 'map',
              'description' : 'A quiet room with large, comfortable chairs. You see a blank map on the table.\n',

            },

            'Parlor' : {
              'directions' : {
                'south' : 'Library',
                'east' : 'Atrium'
              },
              'monster' : 'Red Zombie',
              'description' : 'A nicely decorated room with a \nnumber of chairs arranged in a circle.'
            },

            'Pantry' : {
              'directions' : {
                'west' : 'Kitchen',
                'north' : 'Dining Room'
              },
              'monster' : 'Green Zombie',
              'description' : 'Rows of shelves containing kitchen utensils \nand an ample supply of canned goods.'
            },

            'Guest Bedroom' : {
              'directions' : {
                'south' : 'Dining Room',
                'west' : 'Atrium'
              },
              'poison' : 'hemlock',
              'description' : 'A small, cozy bedroom with a window looking out on the Garden'
            },

            'Garden' : {
              'directions' : {
                'south' : 'Atrium'
              },
              'description' : 'A magnificent, sprawling garden with every \nimaginable type of flower, shrubbery and trees.'
            },

            'Upstairs Hall' : {
              'directions' : {
                'north' : 'Master Bedroom',
                'down' : 'Atrium'
              },
              'description' : 'A narrow upstairs hallway leading to the Master Bedroom. \nThere are stairs leading down.'
            },

            'Master Bedroom' : {
              'directions' : {
                'south' : 'Upstairs Hall',
                'east' : 'Bathroom',
                'west' : 'Office',
                'north' : 'Sun Room'
              },
              'description' : 'A large, luxurious bedroom with a king sized bed and canopy, \nand bedside tables with lamps on both sides.'
            },

            'Office' : {
              'directions' : {
                'east' : 'Master Bedroom'
              },
              'item' : 'key',
              'description' : 'A small room with only a desk, chair and lamp. \nThere is a telephone on the desk.'
            },

            'Bathroom' : {
              'directions' : {
                'west' : 'Master Bedroom'
              },
              'monster' : 'Purple Zombie',
              'description' : 'A bright, clean room with white tiled floor and \nabundant towels neatly folded on a side table.'
            },

            'Sun Room' : {
              'directions' : {
                'south' : 'Master Bedroom'
              },
              'poison' : 'belladonna',
              'description' : 'A beautiful view of the neighboring \nwoods can be see in all directions.'
            }

         }

# start the player in the Hall
currentRoom = 'Hall'
rooms[currentRoom]['position'] = (0,0,0)
traverse_rooms(rooms)

if __name__ == "__main__":

    # Create inventory, which is initially empty
    inventory = []
    visited_rooms = []

    # Initial health points
    health = 3

    showInstructions()
    traverse_rooms(rooms)

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

            if currentRoom not in visited_rooms and 'map' in inventory:
                visited_rooms.append(currentRoom)

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
            if move[1] == "map":
                visited_rooms.append(currentRoom)
            # delete the item from the room
            del rooms[currentRoom]['item']
          # otherwise, if the item isn't there to get
          else:
            # tell player they can't get it
            print('Can\'t get ' + move[1] + '!')

        if move[0] == 'show':
            if "map" in inventory and move[1].lower() == "map":
                map_rooms = {}
                for room in visited_rooms:
                    map_rooms[room] = rooms[room]
                show_map(map_rooms, currentRoom)
            elif "map" not in inventory:
                print("You do not have a map!")

        # Allow command to exit the game
        if move[0] == 'exit':
          break

        # Player loses health if they enter room with Zombie without a Sword
        if 'monster' in rooms[currentRoom] and 'Zombie' in rooms[currentRoom]['monster'] and 'sword' in inventory:
          print('You have defended yourself from the Zombie attack! ... Fantastic!')
        elif 'monster' in rooms[currentRoom] and 'Zombie' in rooms[currentRoom]['monster']:
          # If monster is in room, subtract a health point
          health -= 1
          if health >= 1:
            print("The Zombie took a bite out of you! You need to defend yourself with a sword!")
          else:
            # Game ends once health reaches zero
            print('A Zombie has eaten your brainz ... GAME OVER!!!')
            break

        # Player loses health if they enter room with poison without a potion
        if 'poison' in rooms[currentRoom] and 'potion' in inventory:
          print('The potion has protected you from the Poison! ... Good Deal!')
        elif 'poison' in rooms[currentRoom]:
          # If poison is in room, subtract a health point
          health -= 1
          if health >= 1:
            print("You are weakened by the Poison! A potion will protect you!")
          else:
            # Game ends once health reaches zero
            print('The Poison has killed you ... GAME OVER!!!')
            break

        # Player wins game if they get to the Garden with the key and magic potion
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
          print('You have escaped the house with the Key and Magic Potion ... YOU WIN!!!')
          break
        elif currentRoom == 'Garden':
          print('To escape you need the key and potion ... Keep Looking')

      except KeyboardInterrupt:
        break

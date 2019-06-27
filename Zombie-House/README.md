# Learn Python
[Home](../README.md) | Zombie House

### Zombie House Game

Remix from [original RPG project](https://projects.raspberrypi.org/en/projects/rpg) published by Raspberry Pi Foundation.

**Concepts:**

* Functions
* Lists
* [Dictionaries](dictionaries.md)
* if / else
* for loop
* A "game loop" (using "while True:")
* Formatted String Literals (f-strings)
* try / except

**Objectives:**

Create a text-based game where a player navigates through a set of rooms. Program the rooms to contain items to collect, monsters to avoid and obstacles to overcome. Linking the rooms and populating the items in each room is done in a dictionary. Each room is a nested dictionary inside of the "rooms" dictionary.

```python
# a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                'south' : 'Kitchen',
                'item' : 'key'
            },

            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            }
        }
```
In order to improve the navigation and display the available directions the player can travel, a nested dictionary was introduced so that directions and items are separated (this also fixed a bug in the game).

```python
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
```

Going beyond the original project, this example introduces two new types of objects inside a room: *monster* and *poison* - each being displayed inside the room with the following code:

```python
def showStatus():
  # print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  # print the current inventory
  print('Inventory : ' + str(inventory))
  # print an item, monster or poison if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "monster" in rooms[currentRoom]:
    print('There is a ' + rooms[currentRoom]['monster'] + ' in the room!')
  if "poison" in rooms[currentRoom]:
    print('There is some ' + rooms[currentRoom]['poison'] + ' in the room!')
  print("---------------------------")
  ```
Browse through the code as an example and try making your own text-based adventure game! 

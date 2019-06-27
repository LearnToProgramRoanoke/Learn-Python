# Learn Python
[Home](../README.md) | [Zombie House](README.md) | Dictionaries

### Zombie House Game

**About Dictionaries**

Compared to a list, where items are consectively ordered and accessed by the postion (0, 1, 2, 3, etc), a dictionary is a mapping of items by a key. These key:value pairs are not maintained in any particular order like in a list. The values are simply mapped to the associated key.  Like a list, dictionaries are mutable - values can be added and subtracted in the program.  This is important to the game because items that can be picked up need to be removed from the associated room by taking it out of the dictionary. 

Looking at the original code as an example:

```python
# a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                'south' : 'Kitchen',
                'item' : 'key'
            },

            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'sword'
            }
        }
```

The "rooms" dictionary contains two keys (Hall and Kitchen) that each represents a room. The value for each key is itself a dictionary. This is an important concept - lists and dictionaries both can contain other Python objects. I like to call this "nesting" the dictionaries. It's very handy in developing the game. 

One problem with this dictionary structure was discovered. If the player tries a command like "go item" the game would halt. That's because in the way the game logic works, going to a room should return a key:value pair that has information about the room. An item (such as a sword) does not provide this and causes the crash. 

The solution to this was to break out the directions into a separate key:value pair with the linked rooms inside another dictionary.

```python
rooms = {
            # Each room has a directions key with another dictionary containing the linked rooms
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
              'poison' : 'Hemlock',
              'item' : 'flower'
            },
```

Now, to display the available directions and other items in the room, the "showStatus()" function needs to be modified:

```python
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
```

This same technique could be taken even further to add new items to a room, such as monsters, poisons and other non-playable characters. The downside is, at some point, the entire dictionary becomes hard to manage and maintain.  This leads to the next concept of Object Oriented Programming (OOP).  The objects in the game can be inside a Class and instances created in the program.

More to follow ...
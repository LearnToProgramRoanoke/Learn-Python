# Learn Python
[Home](../README.md) | [Zombie House](README.md) | [Dictionaries](dictionaries.md) | Lists | [Functions](functions.md)

### Zombie House Game

**About Lists**

A list is one of most common objects used in Python. They are very similiar to an array in other languages like C or Java. Lists are an ordered collection of other objects with a zero-based index. In other words, the first item in a list is in position 0, second item in position 1, third item in position 2 and so on. A list is created using the square brackets.

Try this code in the Python REPL:

```python
>>> x = ["one","two","three","four"]
>>> x(0)
>>> 'one'
>>> x(3)
>>> 'four'
```
Lists are mutable, so you can add and remove items in a list in the program. The game uses this for tracking the player's inventory. With the "get [item]" command, if the item is in the room, it is added to the inventory list.

```python
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
```

Notice how the code first checks for the item in the "rooms" dictionary. If found, the item is added to the "inventory" list. Otherwise, a warning is displayed to let the player know they cannot get that specific item.

Look closely at the code that deleted the item from the dictionary.  What problem do you think might occur? This code assumes that there is only one item in the room at a time.

**Challenge**

Consider how the program could be modified to not only get and item, but also drop an item in the player's inventory in another room.

* Before dropping, check that the item is in the inventory list
* Once dropped, add the item to the dictionary for the current room
* Modify the delete code to allow for more than one item in a room

Have fun!
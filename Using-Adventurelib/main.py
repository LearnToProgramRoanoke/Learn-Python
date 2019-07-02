#!/bin/python3

'''
An adaptation of Zombie-House using the Adventurelib library.
https://github.com/lordmauve/adventurelib
MIT License
Copyright (c) 2016 Daniel Pope
Full documentation of Adventurelib is here:
https://adventurelib.readthedocs.io/
This library contains several classes that can be used to create
objects in the game such as rooms, characters and items to be 
placed into the player's inventory
'''
# Place the adventurelib.py file in the root folder and import
from adventurelib import *

# The remaining logic of the game goes before the start() call

# A Bag() is an class used to hold a collection of items
# Create an instance of Bag() for the player's inventory
inventory = Bag()

# Items found in a room will also be using an instance of Bag()
Room.items = Bag()

# Start the game with the player in the Hall using the class Room() 
current_room = Hall = Room(
    """
    You are in the main downstairs hallway.\n
    You see more rooms to the east and west.
    """
)

Dining_Room = Hall.east = Room(
    """
    You are in the dining room. There is a long, majestic\n
    mahagony table in the center of the room.\n
    There is an exit to the west.
    """
)

Library = Hall.west = Room(
    """
    You are in the library.\n
    An impressive collection of very old books.\n
    There is an exit to the east.
    """
)

# Use the Item() class to create objects for the player
# Place items as a property of a room
key = Item('small key','key')
Hall.items = Bag({key,})

sword = Item('broad sword','sword')
Dining_Room.items = Bag({sword,})

potion = Item('magic potion','potion')
Library.items = Bag({potion,})

# the @when decorator allows you to code what happens when a command is entered
# use @when to code going in a direction, taking an item and looking for items
@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say(f'You go {direction}.')
        look()

@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say(f'You pick up the {obj}.')
        inventory.add(obj)
    else:
        say(f'There is no {item} here.')

@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say(f'A {i} is here.')

@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

# Start the game
look()
start()

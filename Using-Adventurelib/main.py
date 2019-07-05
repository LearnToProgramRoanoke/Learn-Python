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

# The remaining logic of the game goes before calling the start() function

# A Bag() is an class used to hold a collection of items
# Create an instance of Bag() for the player's inventory
inventory = Bag()

# Items found in a room will also be using an instance of Bag()
Room.items = Bag()

# Create the items to be found in the game
# Use the Item() class to create objects for the player to find
key = Item('small key','key')
key.carry = True
sword = Item('broad sword','sword')
sword.carry = True
flower = Item('pot of flowers','flower','flowers')
flower.def_name = 'the pot of flowers'
flower.carry = False
potion = Item('magic potion','potion')
potion.carry = True
cheese = Item('block of cheese', 'cheese')
cheese.carry = True
# Also create characters in the game using the Item() class
# Add properties to the character such as health level and weakness in battle
greenZombie = Item('green Zombie','zombie')
greenZombie.def_name = 'the green Zombie'
greenZombie.carry = False
greenZombie.health = 3
greenZombie.weakness = 'sword'

redZombie = Item('red Zombie','zombie')
redZombie.def_name = 'the red Zombie'
redZombie.carry = False
redZombie.health = 3
redZombie.weakness = 'cheese'

# Start the game with the player in the Hall using the class Room() 
current_room = Hall = Room(
    """
    You are in the main downstairs hallway.
    """
)
# Place items as a property of a room
Hall.items = Bag({key,})

# Create the other rooms in the game
Kitchen = Hall.south = Room(
    """
    A large, very clean kitchen. 
    There should be flowers here for decoration.
    """
)
Kitchen.items = Bag({flower,redZombie})

Dining_Room = Hall.east = Room(
    """
    You are in the dining room. There is a long, majestic
    mahagony table in the center of the room.
    """
)
Dining_Room.items = Bag({sword,cheese})

Library = Hall.west = Room(
    """
    You are in the library with
    an impressive collection of very old books.
    """
)
Library.items = Bag({potion,})

Study = Library.south = Room(
    """
    This is the Study.
    A quiet room with large, comfortable chairs.
    """
)
Study.items = Bag({greenZombie,})

Parlor = Library.north = Room(
    """
    A parlor nicely decorated with paintings and 
    number of chairs arranged in a circle.
    """
)

Atrium = Hall.north = Room(
    """
    An atrium with a high, vaulted ceiling.
    """
)

Garden = Atrium.north = Room(
    """
    You are outside of the house in
    a magnificent, sprawling garden with every 
    imaginable type of flower, shrubbery and 
    a number of huge trees.
    """
)

Guest_Bedroom = Dining_Room.north = Room(
    """
    A small, cozy guest bedroom with a window looking out on the Garden.
    """
)

Pantry = Dining_Room.south = Room(
    """
    A pantry with rows of shelves containing kitchen utensils 
    and an ample supply of canned goods.
    """
)

# Create other properties of the rooms, such as exits
Kitchen.west = Study
Pantry.west = Kitchen
Guest_Bedroom.west = Atrium
Parlor.east = Atrium

# Define the actions the player can take in the game
# the @when decorator allows you to code what happens when a command is entered
# use @when to code going in a direction, take/drop an item and look for items
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
@when('get ITEM')
def take(item):
    obj = current_room.items.find(item)
    if obj:
        if obj.carry:
            obj = current_room.items.take(item)
            say(f'You pick up the {obj}.')
            inventory.add(obj)
        else:
            say(f'You can not hold {obj.def_name}')
    else:
        say(f'There is no {item} here.')

@when('drop ITEM')
def drop(item):
    obj = inventory.take(item)
    if not obj:
        say(f'You do not have a {item}.')
    else:
        say(f'You drop the {obj}')
        current_room.items.add(obj)

@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say(f'A {i} is here.')

@when('doors')
def list_exits():
    for exits in current_room.exits():
        say(f'There is a door to the {exits}.')

@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

# Start the game
look()
start()
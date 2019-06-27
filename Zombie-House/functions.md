# Learn Python
[Home](../README.md) | [Zombie House](README.md) | [Dictionaries](dictionaries.md) | [Lists](lists.md) | Functions

### Zombie House Game

**About Functions**

In the most basic description, a function is a block of code that can be called and run as many times as needed in a program. Python uses indentation to establish the block of code. Functions can accept a set of parameters and return a value back to the part of the program that called the function. The format for creating a function uses the "def" keyword:

```python
# Create a new function
def myFirstFunction():
    print("This is my very first function.")
    print("This function does not have any parameters defined.")
    print("And this function does not return any values.")

# Call the new function
myFirstFunction()
```

The first fuction in the Zombie House game simply prints the rules of the game as a block of text:

```python
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
  go [direction]
  get [item]
  exit
  
''')
```

The next function is very important and is used many times over and over in the game loop to display the player status:

```python
def showStatus():
  # print the player's current status
  print('---------------------------')
  print(f"You are in the {currentRoom}")
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
  if "monster" in rooms[currentRoom]:
    print(f"There is a {rooms[currentRoom]['monster']} in the room!")
  if "poison" in rooms[currentRoom]:
    print(f"There is some {rooms[currentRoom]['poison']} in the room!")
  print("---------------------------")
```

**Challenge**

Think about the game could be modified to display the game rules again when the player types "help" at the command prompt. Could there be any other functions introduced to improve the game play?

Keep learning and enjoying your new Python programming skills!
# Learn Python

### Zombie House Game

Remix from [original RPG project](https://projects.raspberrypi.org/en/projects/rpg) published by Raspberry Pi Foundation.

**Concepts:**

* Functions
* Lists
* Dictionaries
* Game Loop

**Objectives:**

Create a text-based game where a player navigates through a set of rooms. Program the rooms to contain items to collect, monsters to avoid and obstacles to overcome. Linking the rooms and populating the items in each room is done in a dictionary. Each room is a nested dictionary inside of the "rooms" dictionary.

```python
# a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                'south' : 'Kitchen'
                'item' : 'key'
            },

            'Kitchen' : {
                'north' : 'Hall'
                'item' : 'monster'
            }
        }
```


"""
Functions for the game map.
"""

def position_lookup(rooms):
    """Make a new dictionary where positions are more accessible. Ordered in a way that will make map printing easier."""

    position_dict = {}
    position_list = {'x':[], 'y':[], 'z':[]}

    for room, value in rooms.items():
        floor = value['position'][2]
        x_value = value['position'][0]
        y_value = value['position'][1]

        position_list['x'].append(x_value)
        position_list['y'].append(y_value)
        position_list['z'].append(floor)

        if floor not in position_dict.keys():
            position_dict[floor] = {}

        if y_value not in position_dict[floor].keys():
            position_dict[floor][y_value] = {}

        position_dict[value['position'][2]][y_value][x_value] = room

    upper_bounds = (max(position_list['x']), max(position_list['y']), max(position_list['z']) )
    lower_bounds = (min(position_list['x']), min(position_list['y']), min(position_list['z']) )

    return position_dict, lower_bounds, upper_bounds

def show_map(rooms, current_room=None):
    """Function to render map to user screen.

    Map only shows rooms which user has visited.
    """
    #print(single_room('Hall', rooms['Hall']['directions'].keys()))
    #print(single_room('Atrium', rooms['Atrium']['directions'].keys()))

    positions, lower_bounds, upper_bounds = position_lookup(rooms)

    position_list = list(positions.keys())

    for floor in reversed(range(lower_bounds[2], upper_bounds[2]+1)):
        print(F'Floor {floor+1}')
        for row in reversed(range(lower_bounds[1], upper_bounds[1]+1)):
            top_line = '\n'
            labels = []
            for col in range(lower_bounds[0], upper_bounds[0]+1):
                try:
                    labels.append(positions[floor][row][col])
                    top_line += '+' + 10*'-' + '+'
                except KeyError:
                    labels.append('')
                    top_line += '-' + 10*'.' + '-'

            next_line = ''
            for char in top_line:
                if char == '+':
                    next_line += '|'
                elif char == '\n':
                    next_line += char
                elif char == '-':
                    next_line += ' '
                else:
                    next_line += '.'

            label_line = '\n'
            for label in labels:
                if label:
                    if label == current_room:
                        label_line += '| ' + label.ljust(10)[:9].upper() + '|'
                    else:
                        label_line += '| ' + label.ljust(10)[:9] + '|'
                else:
                    label_line += 12*' '

            print(top_line + next_line*2 + label_line + next_line*2 + top_line)

def calculate_position(adjoining_position, direction):
    """Calculate position based on an adjoining position and the relative direction of the new position."""

    # Define directions
    directions = {
        'south' : (0, -1, 0),
        'east' : (1, 0, 0),
        'north' : (0, 1, 0),
        'west': (-1, 0, 0),
        'up': (0, 0, 1),
        'down': (0, 0 -1)
    }

    position_vector = directions[direction]

    new_position = tuple([adjoining_position[0] + position_vector[0], adjoining_position[1] + position_vector[1], adjoining_position[2] + position_vector[2]])

    return new_position


def traverse_rooms(rooms, start='Hall', visited_rooms=None, path=None):
    """Goes through rooms dictionary and defines positions relative to starting point. Uses a depth-first search algorithm."""

    if visited_rooms is None:
        visited_rooms = []

    if path is None:
        path = []

    if start not in visited_rooms:
        visited_rooms.append(start)

    path.append(start)

    current_position = rooms[start]['position']

    for direction, joining_room in rooms[start]['directions'].items():
        if joining_room not in visited_rooms:
            room_position = calculate_position(current_position, direction)
            rooms[joining_room]['position'] = room_position
            return traverse_rooms(rooms, visited_rooms=visited_rooms, start=joining_room, path=path)
    try:
        # If we get here, we have found the end of one path and need to backtrace. We backtrace until our path is 0.
        start_room = path[-2]
        del path[-2:]
        return traverse_rooms(rooms, visited_rooms=visited_rooms, start=start_room, path=path)
    except IndexError as e:
        # If we get an index error, that means we have traversed all the rooms!
        return visited_rooms

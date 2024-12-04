import re

# thoughts:
# check in every direction (like queen in chess) starting from every x
# check until either no letters left or you have found your first xmas occurance
# it can be spelled backwards or forwards
# so xmas or samx
# and it can be interrupted (?)

directions = ["up", "down", "left", "right", "up_right", "up_left", "down_right", "down_left"]

with open("4_input.txt") as file:
    first_line = file.readline()
    line_length = len(first_line) - 1 
    content = first_line + file.read()
    content = content.replace("\n", "")


def down(a):
    return a + line_length

def up(a):
    return a - line_length

def left(a):
    return a - 1

def right(a):
    return a + 1

def get_x_coordinate(i):
    return i % line_length

def get_y_coordinate(i):
    return i // line_length

def is_out_of_bounds_vertically(a):
    # this only checks whether it's out of bounds! not whether it's still within the same row
    # therefore, an extra check is needed in the horizontal and diagonal directions
    # vertical should be fine with just this
    return  0 > a or a > len(content) - 1

def wrapped_around(old_i, new_i):
    return get_y_coordinate(new_i) != get_y_coordinate(old_i)


def move_in_dir(i, direction):
    new_i = i 

    if direction == "up":
        new_i = up(i)
        if is_out_of_bounds_vertically(new_i):
            new_i = -1
    elif direction == "down":
        new_i = down(i)
        if is_out_of_bounds_vertically(new_i):
            new_i = -1
    elif direction == "left":
        new_i = left(i)
        if wrapped_around(i, new_i) or new_i < 0:
            new_i = -1
    elif direction == "right":
        new_i =  right(i)
        if wrapped_around(i, new_i) or new_i > len(content) - 1:
            new_i = -1
    elif direction == "up_left":
        new_i = up(left(i))
        if is_out_of_bounds_vertically(new_i) or get_x_coordinate(new_i) > get_x_coordinate(i) or new_i < 0:
            new_i = -1
    elif direction == "up_right":
        new_i =  up(right(i))
        if is_out_of_bounds_vertically(new_i) or get_x_coordinate(new_i) < get_x_coordinate(i) or new_i < 0:
            new_i = -1
    elif direction == "down_left":
        new_i = down(left(i))
        if is_out_of_bounds_vertically(new_i) or get_x_coordinate(new_i) > get_x_coordinate(i) or new_i > len(content) - 1:
            new_i = -1
    elif direction == "down_right":
        new_i =  down(right(i))
        if is_out_of_bounds_vertically(new_i) or get_x_coordinate(new_i) < get_x_coordinate(i) or new_i > len(content) - 1:
            new_i = -1
    else:
        print("huh?")
        new_i = -1

    return new_i

def search_in_direction(i, already_found, direction, word):
    """ Returns True if XMAS is found, False if not """


    if not (0 <= i <= len(content) - 1):
        print("Out of bounds unexpectedly.")
        return False


    # print("dir: ", direction, ", already_found: ", already_found)


    curr_char = content[i]

    if already_found + curr_char == word:
        return True


    new_i = move_in_dir(i, direction)
    if new_i == -1: # word not complete but no letters left to look at, search failed
        return False


    if re.match("^" + already_found + curr_char, word):
        already_found += curr_char
    else:
        return False # I don't get what they meant by overlapping bc this stops the recognition of overlapping words (as I understand them)


    return search_in_direction(new_i, already_found, direction, word)


def search_in_all_directions(i, word):
    count = 0

    for d in directions:
        if search_in_direction(i, "", d, word):
            count += 1

    return count

result = 0
for i in range(0, len(content)):
    c = content[i]
    
    if c == "X":
        result += search_in_all_directions(i, "XMAS")

print(result)


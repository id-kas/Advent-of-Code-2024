class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})" 

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


    def to_index(self):
        return self.y * line_length + self.x

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5




with open("8_example.txt") as file:
    first_line = file.readline()
    line_length = len(first_line)
    content = first_line + file.read()


def to_pos(index):
    return Position(index%line_length, index//line_length)

def is_in_bounds(index):
    return 0 <= index <= len(content) - 1


def move(pos, direction):
    """ Returns direction that it is heading in after this move """
    print(direction)
    if direction == "up":
        pos.y -= 1
        if is_in_bounds(pos.to_index()) and content[pos.to_index()] == "#":
            pos.y += 1
            pos.x += 1
            return "right"
    elif direction == "right":
        pos.x += 1
        if is_in_bounds(pos.to_index()) and content[pos.to_index()] == "#":
            pos.y += 1
            pos.x -= 1
            return "down"
    elif direction == "down":
        pos.y += 1
        if is_in_bounds(pos.to_index()) and content[pos.to_index()] == "#":
            pos.y -= 1
            pos.x -= 1
            return "left"
    elif direction == "left":
        pos.x -= 1
        if is_in_bounds(pos.to_index()) and content[pos.to_index()] == "#":
            pos.y -= 1
            pos.x += 1
            return "up"
    else:
        print("Programmer error")

    return direction


def part_one():
    positions = set()
    
    start_pos = to_pos(content.index("^"))

    direction = "up"

    curr_pos = start_pos
    while is_in_bounds(curr_pos.to_index()):
        positions.add(curr_pos)
        direction = move(curr_pos, direction)
        

    print("Part one: ", len(positions))


part_one()
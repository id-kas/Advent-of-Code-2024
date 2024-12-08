
class Equation():
    def __init__(self, line):
        self.result = line[0]
        self.elements = line[1:]

    def __str__(self):
        return f"{self.result}: {self.elements}"


def read_line_cleanly(line):
    line = (line.strip()).split(" ")
    line[0] = int(line[0][:-1])
    return [int(e) for e in line]



equations = []
with open("7_input.txt") as file:
    for line in file:
        equation = Equation(read_line_cleanly(line))
        # print(equation)
        equations.append(equation)


def is_solveable_rec(equation, current_result, current_index):
    if current_result == equation.result:
        return True
    if current_result > equation.result:
        return False
    if current_index >= len(equation.elements):
        return False

    return is_solveable_rec(equation, current_result + equation.elements[current_index], current_index+1) or \
        is_solveable_rec(equation, current_result * equation.elements[current_index], current_index+1)


def is_solveable(equation):
    return is_solveable_rec(equation, 0, 0)


def part_one():
    result = 0
    for equation in equations:
        if is_solveable(equation):
            result += equation.result

    print("Part one: ", result)



part_one()
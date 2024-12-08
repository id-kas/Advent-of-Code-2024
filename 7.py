
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
        equations.append(equation)


def is_solveable_rec(equation, current_result, current_index):
    if current_result == equation.result and current_index == len(equation.elements):
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


def new_operator(a, b):
    return int(str(a) + str(b))


def is_solveable_rec_2(equation, current_result, current_index):
    if current_result == equation.result and current_index == len(equation.elements):
        return True
    if current_result > equation.result:
        return False
    if current_index >= len(equation.elements):
        return False

    return is_solveable_rec_2(equation, current_result + equation.elements[current_index], current_index+1) or \
        is_solveable_rec_2(equation, current_result * equation.elements[current_index], current_index+1) or \
        is_solveable_rec_2(equation, new_operator(current_result, equation.elements[current_index]), current_index+1) 


def is_solveable_2(equation):
    return is_solveable_rec_2(equation, 0, 0)


def part_two():
    result = 0
    for equation in equations:
        # print(equation)
        if is_solveable_2(equation):
            result += equation.result

    print("Part two: ", result)

part_one()
part_two()

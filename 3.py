import re

mul_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

with open("3_input.txt") as file:
    content = file.read()
    content.replace("\n", "")



def part_one():
    instructions = re.findall(mul_pattern, content)

    result = 0
    for instruction in instructions:
        instruction = instruction[4:-1]
        nums = instruction.split(",")
        result += int(nums[0]) * int(nums[1])

    print("Part 1: ", result)


def part_two():
    instructions = re.findall(mul_pattern + r"|do\(\)|don't\(\)", content)

    active_instructions = []
    active_section = True
    for i in instructions:
        if i == "do()":
            active_section = True
        elif i == "don't()":
            active_section = False
        else: # mul
            if active_section:
                active_instructions.append(i)
            else:
                continue

    result = 0
    for i in active_instructions:
        # print("performing ", mul_instructions_and_pos[pos])

        instruction = i[4:-1]
        nums = instruction.split(",")
        result += int(nums[0]) * int(nums[1])


    print("Part 2: ", result)



part_one()
part_two()
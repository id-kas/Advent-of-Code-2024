

left = []
right = []

with open("1_input.txt") as file:
    for line in file:
        content = (line.strip()).split("   ")
        left.append(int(content[0]))
        right.append(int(content[1]))

left.sort()
right.sort()

def part_one():
    result = 0
    for i in range(0, len(left)):
        result += abs(left[i] - right[i])

    print("Result 1: ", result)



def part_two():
    # calculate sum of left but weigh it depending on how often the given number appears in the right list

    old_num = -1
    factor = 0
    for i in range(0, len(left)):
        num = left[i]

        # already counted occurances of this num
        if num == old_num:
            left[i] *= factor
            continue
        else:
            factor = 0
            # I'm a do this manually since I know that the list is already sorted
            for possible_match in right:
                if possible_match == num:
                    factor += 1
                if possible_match > num:
                    break
            left[i] *= factor
            old_num = num

    result = sum(left)
    print("Result 2: ", result)

# part_one()
part_two()

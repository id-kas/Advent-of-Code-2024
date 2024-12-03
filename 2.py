import time

def ascends(one, two):
    return one < two and abs(one-two) <= 3

def descends(one, two):
    return one > two and abs(one-two) <= 3


def collect_descend_errors(content):
    errors = []
    for i in range(0, len(content) - 1):
        if descends(content[i], content[i+1]):
            continue
        else:
            errors.append(i)
    return errors

def collect_ascend_errors(content):
    errors = []
    for i in range(0, len(content) - 1):
        if ascends(content[i], content[i+1]):
            continue
        else:
            errors.append(i)
    return errors




def part_one():
    unsafe = 0
    report_count = 0
    with open("2_input.txt") as file:
        for line in file:
            report_count += 1
            content = (line.strip()).split(" ")
            for i in range(0, len(content)):
                content[i] = int(content[i])

            if descends(content[0], content[1]): # check if descending
                if len(collect_descend_errors(content)) != 0:
                    unsafe += 1
            else: # check if ascending
                if len(collect_ascend_errors(content)) != 0:
                    unsafe += 1

    print("Result 1: ", report_count - unsafe)

def count_unsafe_orderings(content):
    descend_errors = collect_descend_errors(content)
    ascend_errors = collect_ascend_errors(content)
    return descend_errors if len(descend_errors) < len(ascend_errors) else ascend_errors


#343
def part_two():
    unsafe = 0
    report_count = 0
    with open("2_input.txt") as file:
        for line in file:
            report_count += 1

            content = (line.strip()).split(" ")
            content = [int(num) for num in content]

            errors = count_unsafe_orderings(content)

            if len(errors) == 0: # all is well
                continue

            if len(errors) > 2: # can't be fixed
                unsafe += 1
                continue

            
            # attempt to fix it by removing the element at error index and its neighbors, one at a time
            fixed = False
            og_content = content[:]
            for err in errors: 
                content.pop(err)
                if len(count_unsafe_orderings(content)) == 0:
                    fixed = True
                    break
                content = og_content[:]

                content.pop(err-1)
                if len(count_unsafe_orderings(content)) == 0:
                    fixed = True
                    break
                content = og_content[:]

                content.pop(err+1)
                if len(count_unsafe_orderings(content)) == 0:
                    fixed = True
                    break
                content = og_content[:]

            if not fixed:
                unsafe += 1

    print("Result 2: ", report_count - unsafe)

def part_two_alt():
    unsafe = 0
    report_count = 0
    with open("2_input.txt") as file:
        for line in file:
            report_count += 1

            content = (line.strip()).split(" ")
            content = [int(num) for num in content]

            og_content = content[:]
            safe = False
            for i in range(0, len(content)):
                content.pop(i)
                if len(count_unsafe_orderings(content)) == 0:
                    safe = True 
                content = og_content[:]
            if not safe:
                unsafe += 1

    print("Result 2: ", report_count - unsafe)  



start = time.time()
part_one()
end = time.time()
print(end - start)

part_two()
end = time.time()
print(end - start)

part_two_alt()
end = time.time()
print(end - start)

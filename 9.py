    

def disk_map_to_file_blocks(disk_map):
    """Comverts the disk map to file block representation
        e.g. 123 ==> 0..111"""

    file_blocks = []
    lowest_usable_id = 0
    for i in range(0, len(disk_map)):
        if i % 2 == 0:
            new_block = [lowest_usable_id for i in range(0, int(disk_map[i]))]
            file_blocks.append(new_block)
            lowest_usable_id += 1
        else:
            if disk_map[i] != "0": # to avoid entries for the case "no gap between storage blocks"
                file_blocks.append(["." for i in range(0, int(disk_map[i]))])

    return file_blocks

def check_sum(file_blocks):
    index = 0
    checksum = 0
    for block_group in file_blocks:
        for block in block_group:
            checksum += index * block
            index += 1
    return checksum

def is_empty_block(block):
    return "." in block 

def lowest_empty(file_blocks):
    for i in range(0, len(file_blocks)):
        if is_empty_block(file_blocks[i]):
            return (i, 0)
    print("Disk map is completely full")
    return None

def highest_non_empty(file_blocks):
    for i in range(len(file_blocks) - 1, -1, -1):
        if not is_empty_block(file_blocks[i]):
            return (i, len(file_blocks[i]) - 1)
    print("Disk map is empty")
    return None


def swap(file_blocks, src, dst):
    """ expects arguments to be in format [index of block, index within block] """
    val = file_blocks[src[0]][src[1]]

    file_blocks[src[0]].pop(src[1])
    if len(file_blocks[src[0]]) == 0:
        file_blocks.pop(src[0])


    file_blocks[dst[0]].pop(dst[1])
    if len(file_blocks[dst[0]]) == 0:
        file_blocks.pop(dst[0])


    # check for adjacent regions of same storage id 
    if val in file_blocks[dst[0] - 1]:
        file_blocks[dst[0] - 1].append(val)
    elif not dst[0] >= len(file_blocks) - 1 and val in file_blocks[dst[0] + 1]:
        file_blocks[dst[0] + 1].append(val)
    # if none exist, it gets a new block
    else:
        file_blocks.insert(dst[0], [val])



def part_one():
    while True:

        highest= highest_non_empty(file_blocks)
        lowest = lowest_empty(file_blocks)

        # if lowest is None that means the storage blocks have no more gaps left
        if lowest is None or highest[0] < lowest[0]:  
            while is_empty_block(file_blocks[-1]):
                file_blocks.pop(-1)
            if file_blocks[-2][0] in file_blocks[-1]:
                file_blocks[-2] = file_blocks[-2] + file_blocks[-1]
                file_blocks.pop(-1)

            break

        swap(file_blocks, highest, lowest)

        # print(file_blocks)



    # print(file_blocks)

    checksum = check_sum(file_blocks)
    print("Part one:", checksum)




with open("9_input.txt") as file:
    content = file.read()

file_blocks = disk_map_to_file_blocks(content)
part_one()
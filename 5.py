
import re

order_rules = {}

reports = []


with open("5_input.txt") as file:
    for line in file:
        if re.match(r"[0-9]+\|[0-9]+", line):
            rule = line.split("|")
            if int(rule[0]) not in order_rules:
                order_rules[int(rule[0])] = [int(rule[1])]
            else:
                order_rules[int(rule[0])].append(int(rule[1]))
            # print(rule[0], rule[1])
        elif not line.strip() == "":
            nums = [int(num) for num in line.split(",")]
            reports.append(nums)
            # print(nums)
        else:
            print(f"Skipped line: {line}")
            continue

# print(order_rules)

def check_if_report_valid(report):
    for i in range(0,len(report)):
        curr_page = report[i]
        if curr_page not in order_rules:
            continue

        # print(order_rules[curr_page])


        for j in range(0, i):
            # order_rules[curr_page] are all the pages that have to be after curr_page or not exist at all
            if report[j] in order_rules[curr_page]: 
                return False

    return True


def get_middle(report):
    return report[len(report)//2]

def part_one():
    result = 0
    for r in reports:
        if check_if_report_valid(r):
            result += get_middle(r)
            print(get_middle(r))

    print("Part one: ", result)

def fix_report(report):
    while not check_if_report_valid(report):
        for i in range(0, len(report)):
            page = report[i]
            if page not in order_rules:
                report.pop(i)
                report.append(page)
            else:
                for larger_page in order_rules[page]:
                    if larger_page not in report:
                        continue
                    larger_page_i = report.index(larger_page)
                    if larger_page_i < i:
                        report.pop(larger_page_i)
                        report.insert(i+1, larger_page)

def part_two():
    result = 0
    for r in reports:
        if not check_if_report_valid(r):
            fix_report(r)
            result += get_middle(r)
            print(get_middle(r))

    print("Part two: ", result)


# part_one()
part_two()

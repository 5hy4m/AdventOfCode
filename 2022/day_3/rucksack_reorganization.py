def solution(input):
    rucksacks = input.split("\n")[:-1]
    matching_char_arr = []
    for rucksack in rucksacks:
        half_length = len(rucksack) // 2
        first_segment, second_segment = [rucksack[:half_length], rucksack[half_length:]]
        matching_char_arr.append(find_matching_char(first_segment, second_segment))
    return sum_priorities(matching_char_arr)


def sum_priorities(arr):
    sum = 0
    for char in arr:
        if char.isupper():
            sum += ord(char) - 38
        else:
            sum += ord(char) - 96
    return sum


def find_matching_char(first_segment, second_segment):
    for i, f in enumerate(first_segment):
        for j, s in enumerate(second_segment):
            if first_segment[i] == second_segment[j]:
                return first_segment[i]


def solution_part2(input):
    rucksacks = input.split("\n")[:-1]
    grouped_elves = []
    group = []
    for i, rucksack in enumerate(rucksacks):
        if i != 0 and i % 3 == 0:
            grouped_elves.append(group)
            group = []
        group.append(rucksack)
    grouped_elves.append(rucksacks[-3:])

    matching_chars = []
    for grp in grouped_elves:
        matching_chars.append(find_matching_char_in_group(grp))

    return sum_priorities(matching_chars)


def find_matching_char_in_group(group):
    for char in group[0]:
        if char in group[1]:
            if char in group[2]:
                return char

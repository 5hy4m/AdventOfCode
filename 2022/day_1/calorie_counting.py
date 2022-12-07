def solution(input):
    input = input.split("\n")
    calories_per_elf = []
    total_calories_of_current_elf = 0
    top_elves_count = 3

    for data in input:
        if data != "":
            total_calories_of_current_elf += int(data)
        else:
            calories_per_elf.append(total_calories_of_current_elf)
            total_calories_of_current_elf = 0

    calories_per_elf.sort(reverse=True)
    return sum(calories_per_elf[:top_elves_count])

from day_3.rucksack_reorganization import solution, solution_part2

txtFile = open("./2022/day_3/input.txt", "r")
input = txtFile.read()

# Tests
def test_scenario1():
    assert solution(input) == 8018


def test_scenario2():
    assert solution_part2(input) == 2518

from day_2.rock_paper_scissors import solution, solution_part2

txtFile = open("./2022/day_2/input.txt", "r")
input = txtFile.read()

# Tests
def test_scenario1():
    assert solution(input) == 11386


def test_scenario2():
    assert solution_part2(input) == 13600

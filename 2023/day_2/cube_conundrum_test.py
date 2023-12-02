from cube_conundrum import solution

txtFile = open("./2023/day_2/input.txt", "r")
input = txtFile.read()


# Tests
def test_scenario1():
    assert solution(input) == 69110

from trebuchet import solution

txtFile = open("./2023/day_1/input.txt", "r")
input = txtFile.read()


# Tests
def test_scenario1():
    assert solution(input) == 54591

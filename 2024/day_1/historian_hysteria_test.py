from historian_hysteria import solution

txtFile = open("./2024/day_1/input.txt", "r")
input = txtFile.read()


# Tests
def test_scenario1():
    assert solution(input) == 1506483
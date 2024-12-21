from red_nosed_reports import solution

txtFile = open("./2024/day_2/input.txt", "r")
input = txtFile.read()


# Tests
def test_scenario1():
    assert solution(input) == 479

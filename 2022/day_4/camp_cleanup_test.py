from day_4.camp_cleanup import solution

txtFile = open("./2022/day_4/input.txt", "r")
input = txtFile.read()
# Tests
def test_scenario1():
    assert solution(input) == (456, 808)

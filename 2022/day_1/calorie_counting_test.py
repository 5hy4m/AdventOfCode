from day_1.calorie_counting import solution

txtFile = open("./2022/day_1/input.txt", "r")
input = txtFile.read()

# Tests
def test_scenario1():
    assert solution(input) == 205370

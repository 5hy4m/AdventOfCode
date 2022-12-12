from day_5.supply_stacks import Solution

txtFile = open("./2022/day_5/input.txt", "r")
input = txtFile.read()

# Tests
def test_scenario1():
    assert Solution().part1(input) == ("GRTSWNJHH", "QLFQDBBHM")

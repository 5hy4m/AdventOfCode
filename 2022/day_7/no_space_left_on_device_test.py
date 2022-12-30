from day_7.no_space_left_on_device import Phone

txtFile = open("./2022/day_7/input.txt", "r")
input = txtFile.read()

# Tests
def test_scenario1():
    assert Phone(input).free_space() == 5

from day_6.tuning_trouble import solution

txtFile = open("./2022/day_6/input.txt", "r")
input = txtFile.read()

# Tests
def test_scenario1():
    assert solution("bvwbjplbgvbhsrlpgdmjqwftvncz")[0] == 5


def test_scenario2():
    assert solution("nppdvjthqldpwncqszvftbrmjlhg")[0] == 6


def test_scenario3():
    assert solution("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")[0] == 10


def test_scenario4():
    assert solution("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")[0] == 11


def test_scenario5():
    assert solution(input)[0] == 1850


def test_scenario6():
    assert solution("mjqjpqmgbljsphdztnvjfqwrcgsmlb")[1] == 19


def test_scenario7():
    assert solution(input)[1] == 2823

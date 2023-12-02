import sys


# Part ONE
# def solution(input):
#     input = input.split("\n")
#     summation = 0
#     for s in input:
#         calibration_value = ""
#         for char in s:
#             if char.isdigit():
#                 calibration_value += char
#                 break

#         for i in range(len(s) - 1, -1, -1):
#             if s[i].isdigit():
#                 calibration_value += s[i]
#                 break
#         if calibration_value:
#             summation += int(calibration_value)
#     return summation


# Part TWO
def solution(input):
    input = input.split("\n")
    summation = 0
    word_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for s in input:
        first_digit = None
        first_digit_index = sys.maxsize - 1
        second_digit_index = -sys.maxsize
        second_digit = None

        for i, char in enumerate(s):
            if char.isdigit():
                if i < first_digit_index:
                    first_digit_index = i
                    first_digit = int(s[i])
                elif i > second_digit_index:
                    second_digit_index = i
                    second_digit = int(s[i])
            if second_digit is None:
                second_digit = first_digit
                second_digit_index = first_digit_index

        for digit in word_digits:
            lowest_starting_index = s.find(digit)
            highest_starting_index = s.rfind(digit)
            if lowest_starting_index != -1:
                if lowest_starting_index < first_digit_index:
                    first_digit_index = lowest_starting_index
                    first_digit = word_digits[digit]
                elif lowest_starting_index > second_digit_index:
                    second_digit_index = lowest_starting_index
                    second_digit = word_digits[digit]

            if highest_starting_index != -1:
                if highest_starting_index < first_digit_index:
                    first_digit_index = highest_starting_index
                    first_digit = word_digits[digit]
                elif highest_starting_index > second_digit_index:
                    second_digit_index = highest_starting_index
                    second_digit = word_digits[digit]

        if first_digit is not None and second_digit is not None:
            print(s, int(str(first_digit) + str(second_digit)))
            summation += int(str(first_digit) + str(second_digit))

    return summation
    # for index in indexes:
    #     if index < first_digit:
    #         first_digit = index
    #     if index > second_digit:
    #         second_digit = index

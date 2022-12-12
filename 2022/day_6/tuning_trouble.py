def solution(input):
    part1 = getSubroutine(input, 4)
    part2 = getSubroutine(input, 14)
    return part1, part2


def getSubroutine(input, length):
    p1 = 0
    p2 = 1

    while p2 < len(input) or len(input[p1 : p2 + 1]) == length:
        if p1 == p2:
            p2 += 1

        if input[p2] in input[p1:p2]:
            p1 += 1
            continue

        if len(input[p1 : p2 + 1]) == length:
            p2 += 1
            break
        p2 += 1
    return p2

def solution(input):
    input = input.split("\n")

    safeCount = 0
    for report in input:
        report = report.split(" ")

        if len(report) <= 1:
            continue
        l = 0
        r = 1
        isIncrease = True if int(report[r]) - int(report[l]) > 0 else False
        while r <= len(report) - 1:
            level = int(report[r]) - int(report[l])
            isZero = level == 0
            if isZero:
                break
            if isIncrease:
                if level > 0 and level <= 3:
                    r += 1
                    l += 1
                    continue
            else:
                if level < 0 and abs(level) > 0 and abs(level) <= 3:
                    r += 1
                    l += 1
                    continue
            break
        else:
            safeCount += 1
    return safeCount

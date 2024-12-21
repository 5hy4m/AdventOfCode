def solution(input):
    input = input.split("\n")

    safeCount = 0
    for report in input:
        report = report.split(" ")

        if validReport(report):
            safeCount += 1
        else:
            print("Actual: ", report)
            for i in range(len(report)):
                print("Iterations: ", report[:i] + report[i + 1 :], i)
                if validReport(report[:i] + report[i + 1 :]):
                    print("Selected: ", report[:i] + report[i + 1 :])
                    safeCount += 1
                    break
    return safeCount


def validReport(report):
    if len(report) <= 1:
        return False
    l = 0
    r = 1
    isIncrease = True if int(report[r]) - int(report[l]) > 0 else False
    while r <= len(report) - 1:
        level = int(report[r]) - int(report[l])
        isZero = level == 0
        if isZero:
            return False
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
        return True

from collections import defaultdict

def solution(input):
    input = input.split("\n")

    rArr,lArr = [],[]

    for num in input:
        l,r = num.split("   ")
        lArr.append(int(l))
        rArr.append(int(r))
    
    counterDict = defaultdict(int)
    for r in rArr:
        counterDict[r] += 1
    res = 0
    for l in lArr:
        res += l * counterDict[l]
    return res

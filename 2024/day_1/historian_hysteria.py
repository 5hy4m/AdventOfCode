def solution(input):
    input = input.split("\n")

    rArr,lArr = [],[]

    for num in input:
        l,r = num.split("   ")
        lArr.append(int(l))
        rArr.append(int(r))
    
    lArr.sort()
    rArr.sort()

    res = 0
    print(len(lArr))
    for i in range(len(lArr)):
        print(i)
        diff = abs(lArr[i]-rArr[i])
        # print(lArr[i],rArr[i],diff)
        res += diff

    return res

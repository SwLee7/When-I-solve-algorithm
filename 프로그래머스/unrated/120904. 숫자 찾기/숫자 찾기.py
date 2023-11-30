def solution(num, k):
    numArr = str(num)
    for i in range(len(numArr)):
        if numArr[i] == str(k):
            return i + 1
    return -1
        
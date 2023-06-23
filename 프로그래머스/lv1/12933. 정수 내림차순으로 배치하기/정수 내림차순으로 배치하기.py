def solution(n):
    li = list(str(n))
    li.sort()
    li.reverse()
    result = ''.join(li)
    return int(result)
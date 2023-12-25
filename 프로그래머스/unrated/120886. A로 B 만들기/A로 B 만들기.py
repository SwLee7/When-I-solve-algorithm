def solution(before, after):
    answer = 0
    b = list(before)
    a = list(after)
    b.sort()
    a.sort()
    if b == a:
        answer = 1
    return answer
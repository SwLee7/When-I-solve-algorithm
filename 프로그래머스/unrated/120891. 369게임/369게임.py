def solution(order):
    answer = 0
    arr = [int(a) for a in str(order)]
    for i in arr:
        if i == 3 or i == 6 or i == 9:
            answer += 1
    return answer
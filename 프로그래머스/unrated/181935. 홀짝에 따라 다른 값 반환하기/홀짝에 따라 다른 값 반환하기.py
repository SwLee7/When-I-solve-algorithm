def solution(n):
    answer = 0
    for i in range(1, n+1, 2):
        if n % 2 == 0:
            answer += (i+1)**2
        else :
            answer += i
    return answer
def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    boxes = len(score) // m
    
    for i in range(boxes):
         answer += min(score[m*i : m*i + m]) * m
    
    return answer
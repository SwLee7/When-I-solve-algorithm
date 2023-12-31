def solution(answers):
    answer = []
    
    ran_1_score, ran_2_score, ran_3_score = 0, 0, 0
    
    ran_1 = [1,2,3,4,5]
    ran_2 = [2,1,2,3,2,4,2,5]
    ran_3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == ran_1[i % len(ran_1)]:
            ran_1_score += 1
        if answers[i] == ran_2[i % len(ran_2)]:
            ran_2_score += 1
        if answers[i] == ran_3[i % len(ran_3)]:
            ran_3_score += 1
            
    highest_score = max(ran_1_score, ran_2_score, ran_3_score)
    
    if ran_1_score == highest_score:
        answer.append(1)
    if ran_2_score == highest_score:
        answer.append(2)
    if ran_3_score == highest_score:
        answer.append(3)
    
    return answer
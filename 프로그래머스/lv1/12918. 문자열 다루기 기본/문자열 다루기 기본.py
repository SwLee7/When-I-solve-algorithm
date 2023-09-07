def solution(s):
    answer = True
    for i in range(len(s)) :
        if len(s) == 4 or len(s) == 6:
            if s.isdigit() == True :
                answer = answer
            else : 
                answer = False
        else :
            answer = False        
    return answer
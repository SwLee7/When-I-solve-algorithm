def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        answer.append(num_list[i])
    for i in range(len(answer)):
        if answer[-1] > answer[-2]:
            answer.append(answer[-1] - answer[-2])
            break
        else : 
            answer.append(int(answer[-1]) * 2)
            break
    return answer
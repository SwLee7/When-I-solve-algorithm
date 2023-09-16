def solution(num_list):
    mul = 1
    answer = 0
    for i in num_list:
        mul *= i
        if mul < sum(num_list)*sum(num_list):
            answer = 1
        else :
            answer = 0
    return answer
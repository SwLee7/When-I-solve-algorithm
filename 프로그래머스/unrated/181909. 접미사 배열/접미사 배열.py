def solution(my_string):
    answer = []
    answer = sorted(my_string[i:] for i in range(len(my_string)))
    return answer

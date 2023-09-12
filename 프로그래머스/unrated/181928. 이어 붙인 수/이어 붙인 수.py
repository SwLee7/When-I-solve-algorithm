def solution(num_list):
    answer = 0
    sum_even = ''
    sum_odd = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            sum_even += str(num_list[i])
        else :
            sum_odd += str(num_list[i])
    answer = int(sum_odd) + int(sum_even)
    return answer
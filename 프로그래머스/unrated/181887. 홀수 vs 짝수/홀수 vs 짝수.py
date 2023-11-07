def solution(num_list):
    sum_odd = sum(num_list[i] for i in range(0, len(num_list), 2))
    sum_even = sum(num_list[i] for i in range(1, len(num_list), 2))
    return sum_odd if  sum_odd >= sum_even else sum_even
def solution(array):
    answer = []
    largest_number = max(array)
    largest_number_index = array.index(max(array))
    answer.append(largest_number)
    answer.append(largest_number_index)
    return answer
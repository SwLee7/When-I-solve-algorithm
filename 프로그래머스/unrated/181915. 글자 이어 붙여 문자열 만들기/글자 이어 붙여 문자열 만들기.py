def solution(my_string, index_list):
    answer = []
    list_my_string = list(my_string)
    for i in range(len(index_list)):
        answer.append(list_my_string[index_list[i]])
    return "".join(answer)
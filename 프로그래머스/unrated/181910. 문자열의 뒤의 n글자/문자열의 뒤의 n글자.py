def solution(my_string, n):
    x = len(my_string)
    y = x - n
    return my_string[y:x]
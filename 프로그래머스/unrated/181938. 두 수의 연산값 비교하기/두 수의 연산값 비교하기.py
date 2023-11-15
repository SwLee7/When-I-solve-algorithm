def solution(a, b):
    answer = 0
    operator_x = int(str(a)+str(b))
    if operator_x < 2*a*b:
        answer = 2*a*b
    else:
        answer = operator_x
    return answer
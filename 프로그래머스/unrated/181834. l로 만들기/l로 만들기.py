def solution(myString):
    answer = [a if a > 'l' else 'l' for a in myString]
    return "".join(answer)
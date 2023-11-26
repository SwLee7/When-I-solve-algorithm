def solution(myString):
    cnt = myString.split('x')
    return [len(i) for i in cnt]
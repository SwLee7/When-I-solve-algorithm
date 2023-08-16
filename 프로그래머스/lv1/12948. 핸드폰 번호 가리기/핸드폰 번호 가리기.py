def solution(phone_number):
    n = len(phone_number)
    opened = phone_number[-4:]
    answer = '*'*(n-4) + opened
    return answer
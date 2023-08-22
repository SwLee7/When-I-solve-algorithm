def solution(numbers):
    n = 0
    for i in range(10):
        if i not in numbers:
            n += i
    return n
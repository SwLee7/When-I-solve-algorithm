from math import factorial as fct
def solution(balls, share):
    n = fct(balls)
    m = fct(share)
    k = fct(balls - share) * m
    return n / k
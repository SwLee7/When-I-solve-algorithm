def solution(price, money, count):
    x = 0
    for i in range(1, count+1):
        x += price * i
    if x < money :
        x =  0
    else :
        x = x - money            
    return x
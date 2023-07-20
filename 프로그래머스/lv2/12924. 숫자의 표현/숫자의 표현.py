def solution(n):
    arr = []
    for i in range(1,n+1,2):
        if n % i == 0:
            arr.append(i)
    return len(arr)
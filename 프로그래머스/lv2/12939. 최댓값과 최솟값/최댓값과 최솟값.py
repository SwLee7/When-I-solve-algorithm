def solution(s):
    new = list(map(int, s.split(" ")))
    return (str(min(new)) + " " + str(max(new)))
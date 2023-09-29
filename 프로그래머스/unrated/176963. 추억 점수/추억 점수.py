def solution(name, yearning, photo):
    answer = []
    for i in photo:
        sum_point = 0
        for j in i:
            if j in name:
                sum_point += yearning[name.index(j)]
        answer.append(sum_point)
    return answer
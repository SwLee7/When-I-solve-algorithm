def solution(numbers):
    list_answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            list_answer.append(numbers[i] + numbers[j])
    answer = sorted(set(list_answer))
    return answer
def solution(strings, n):
	# x[n] 을 기준으로 정렬하고 같을 시, x 를 기준으로 정렬하기
    return sorted(strings, key=lambda x:(x[n], x))
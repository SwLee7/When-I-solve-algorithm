def solution(bin1, bin2):
    temp1 = int (bin1, 2)
    temp2 = int (bin2, 2)
    answer = bin(temp1 + temp2)
    return answer.replace("0b","")
# bin()을 이용해서 이진수로 바꾸면 '0b'가 생겨서 replace()를 이용해 제거 후 return
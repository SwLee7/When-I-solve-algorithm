import re
# 정규 표현식을 import
def solution(my_string):
    my_string = re.sub('[a-zA-Z]',' ',my_string)
    num_list = list(map(int, my_string.split()))
    return sum(num_list)
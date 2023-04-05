function solution(my_string) {
    let answer = '';
    //1. 문자열을 배열화-split을 이용
    let arr = my_string.split('');
    let reverseArr = arr.reverse();
    answer = reverseArr.join('');
    return answer;
}
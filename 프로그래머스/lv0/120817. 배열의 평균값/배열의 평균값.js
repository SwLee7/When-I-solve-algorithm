function solution(numbers) {
    var answer = 0;
    for (let i=0 ; i<numbers.length ; i++){
        answer = (numbers[0]+numbers[numbers.length-1])/2
    }
    return answer;
}
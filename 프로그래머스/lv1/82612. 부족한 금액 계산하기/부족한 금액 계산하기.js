function solution(price, money, count) {
    let answer = 0
    for (let i = 1 ; i < count +1 ; i++){
        answer += price * i
    } if (answer > money) {
        answer = answer - money
    } else {
        answer = 0
    } return answer
}
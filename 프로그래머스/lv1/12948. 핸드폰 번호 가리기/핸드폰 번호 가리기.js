function solution(phone_number) {
    let opened = phone_number.slice(-4);
    let n = phone_number.length;
    let answer = "*".repeat(n-4) + opened;
    return answer;
}
function solution(n, k) {
    // 10인분 음료수 1개 공짜
    // 양꼬치 1인분에 12,000-n, 음료수 1개-k 1,000
    
    //n을 10으로 나눈 몫이 서비스 음료수 개수;
    //Math.floor(n/10)
    var answer = 0;
    answer = 12000*n + 2000*(k - Math.floor(n/10))
    return answer;
}
function solution(n, words) {
    let answer = [0,0];
    let cnt = 0;
    let add = [];
    add.push(words[0]);
    for (let i=1 ; i < words.length ; i++){
        cnt += 1;
        if (!add.includes(words[i]) && words[i-1][words[i-1].length-1] === words[i][0]){
            add.push(words[i]);
        } else {
            answer[0] = cnt % n + 1;
            answer[1] = Math.floor(cnt / n) +1
            break;
        }
    }
    return answer;
}
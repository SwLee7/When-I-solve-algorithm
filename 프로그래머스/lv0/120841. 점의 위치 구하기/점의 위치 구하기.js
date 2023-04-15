function solution(dot) {
    // dot은 arr[x,y]
    let answer = 0;
    if (0 < dot[0] && 0 < dot[1]) answer = 1;
    if (dot[0] < 0 && 0 < dot[1]) answer = 2;
    if (0 < dot[0] && dot[1] < 0) answer = 4;
    if (dot[0] < 0 && dot[1] < 0) answer = 3;
    return answer;
}
function solution(angle) {
    //angle <90; 예각, =90; 직각, 90~179 둔각, 180 평각
    // 예각일 때 변수를 a, 직각일 떄 변수를 r, 둔각일 때 b, 평각일 때 p
    let answer = 0;
    for (let i=0 ; i <=angle ; i+=1){
        if (angle < 90){
            answer = 1;
        } else if (angle === 90){
            answer = 2;
        } else if (angle > 90 && angle < 180){
            answer = 3;
        } else if (angle === 180){
            answer = 4;
        }
    }
    return answer;
}
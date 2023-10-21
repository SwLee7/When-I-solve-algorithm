function solution(sizes) {
    var answer = 0;
    var w = [];
    var h = [];
    for (let i = 0 ; i < sizes.length ; i++){
        if (sizes[i][0] >= sizes[i][1]){
            w.push(sizes[i][0]);
            h.push(sizes[i][1]);
        } else {
            h.push(sizes[i][0]);
            w.push(sizes[i][1]);
        }
    answer = Math.max(...h) * Math.max(...w)
    }
    return answer;
}
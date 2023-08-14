function solution(people, limit) {
    let answer = 0;
    people.sort((x, y) => x - y);
    let a = 0
    let b = people.length - 1;
    while( a < b ) {
        if (people[a] + people[b] <= limit) {
            a ++
            answer ++ 
        }
        b --;
    }
    return people.length - answer;
}
function solution(num_list) {
    var answer = 0;
    sum_odd = 0;
    sum_even = 0;
    for (let i = 0 ; i < num_list.length ; i += 2) {
        sum_odd += num_list[i];
    }
    for (let j = 1; j < num_list.length ; j += 2) {
        sum_even += num_list[j];
    }
    if (sum_odd >= sum_even) {
        answer = sum_odd;
    } else {
        answer = sum_even;
    }
    return answer;
}
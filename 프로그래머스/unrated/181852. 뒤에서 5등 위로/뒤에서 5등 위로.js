function solution(num_list) {
    num_list.sort((x,y) => x - y)
    return num_list.slice(5)
}
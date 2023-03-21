function solution(array) {
    array = array.sort(function compareNumbers(a, b) {
  return a - b;
})
    return array[Math.floor(array.length / 2)] 
}
function solution(numbers) {
   let arr = numbers.sort(function(a, b)  {
  return a - b;
});
    let a = arr[arr.length-1]*arr[arr.length-2]
    return a;
}
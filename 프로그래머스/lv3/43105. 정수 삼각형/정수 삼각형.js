const solution = (triangle) => {
  let answer = 0;
  const column = triangle.length;
  for (let i = 1; i < column; i++) {
    for (let j = 0; j < triangle[i].length; j++) {
      if (j === 0) {
        triangle[i][j] += triangle[i - 1][j];
      } else if (j === triangle[i].length - 1) {
        triangle[i][j] += triangle[i - 1][j - 1];
      } else {
        triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
      }
    }
  }
  for (let i = 0; i < triangle[column - 1].length; i++) {
    if (answer < triangle[column - 1][i]) {
      answer = triangle[column - 1][i];
    }
  }

  return answer;
};
function caixa(values) {
  const length = values.shift();
  const validNumbers = [];

  values.map((num) => {
    if (num !== 0) {
      validNumbers.push(num);
    }
    if (num === 0) {
      validNumbers.pop();
    }
  })
  return validNumbers.reduce((pre, cur) => cur + pre, 0);
}

console.log(caixa([10, 1, 3, 5, 4, 0, 0, 7, 0, 0, 6]));
// expected 7
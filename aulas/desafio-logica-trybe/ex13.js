const numberToArray = (number) => {
    const array = String(number).split("");
    return array.map((n) => Number(n));
}

function digits_sum(number_s) {
    let sumOfNumbers = 0;
    const selectedNums = [];
    for (let index = 0; index < 1000; index += 1) {
        sumOfNumbers = numberToArray(index).reduce((pre, cur) => pre + cur, 0);
        if (sumOfNumbers === number_s) {
            selectedNums.push(index);
        }
    }
    return selectedNums.length;
}

console.log(digits_sum(26));
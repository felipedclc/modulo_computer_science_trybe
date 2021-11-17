const isPrime = (num) => {
  if (num === 2) return true;

  for (let index = 2; index < num; index += 1) {
    if (num % index === 0) return false
    return true
  }
}

function nth_prime(n) {
  const prime_numbers = [];
  let number = 2;
  while (prime_numbers.length <= n) {
    if (isPrime(number)) {
      prime_numbers.push(number);
    }
    number += 1;
  }
  return prime_numbers;
}

console.log(nth_prime(9));
// console.log(isPrime(7));
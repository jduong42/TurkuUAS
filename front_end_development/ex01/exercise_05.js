const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

numbers.push(11, 12, 13, 14, 15);

console.log(numbers); // Working on original array

const copy_numbers = numbers.slice(0, 5); // Copying the first 5 elements of the original array to a new array

console.log(numbers)
console.log(copy_numbers); // Working on a copy of the original array
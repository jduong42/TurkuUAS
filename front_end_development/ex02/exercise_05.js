// Function with default parameter value

function greet(name = 'Guest') {
    console.log('Hello, ' + name + '!');
}

// Calling the function with and without a parameter
greet('John');
greet();

// Function using rest parameters

function sum(...numbers) {
    let result = 0;
    for (let number of numbers) {
        result = result + number;
    }
    return result;
}

// Calling the function with different numbers of arguments

console.log(sum(1, 2, 3)); // Output: 6
console.log(sum(1, 2, 3, 4, 5)); // Output: 15
console.log(sum(10)); // Output: 10
console.log(sum()); // Output: 0 (no arguments)

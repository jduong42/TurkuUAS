// Function with default parameter value

function greet(name = 'Guest') {
    console.log('Hello, ' + name + '!');
}

// Calling the function with and without a parameter
greet('John');
greet();
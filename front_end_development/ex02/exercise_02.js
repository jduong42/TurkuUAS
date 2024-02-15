var containsNumber = function (numbers, aNumber) {

    let counter = 0;

    for (let i = 0,len_list = numbers.length; i < len_list; i++) {
        if (numbers[i] === aNumber) {
            counter++;
            return true;
        }
    }
    if (counter== 0) {
        return false;
    }
}

// This part is copied almost from exercise_01.html -file.

function displayResult(number, contains) {
    var resultDiv = document.getElementById('result');
    if (contains) {
        resultDiv.textContent = "The list contains the number " + number;
    } else {
        resultDiv.textContent = "The list does not contain the number " + number;
    }
}

function checkNumber() {
    var numberInput = document.getElementById('numberInput').value;
    var number = parseInt(numberInput);
    var numbers = [6, 4, 2, 5, 9, 7, 5, 7, 2];
    var contains = containsNumber(numbers, number);
    if (!isNaN(number)) {
        displayResult(number, contains);
    } else {
        alert("Please enter a valid number!");
    }
}
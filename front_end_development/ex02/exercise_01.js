function isLeapYear(year) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        return true;
    }
    else {
        return false;
    }
}

// This part is from ChatGPT.

function displayResult(year, isLeap) {
    var resultDiv = document.getElementById('result');
    if (isLeap) {
        resultDiv.textContent = "Year " + year + " is a leap year";
    } else {
        resultDiv.textContent = "Year " + year + " is not a leap year";
    }
}

function checkYear() {
    var yearInput = document.getElementById('yearInput').value;
    var year = parseInt(yearInput);
    if (!isNaN(year)) {
        var isLeap = isLeapYear(year);
        displayResult(year, isLeap);
    } else {
        alert("Please enter a valid year!");
    }
}
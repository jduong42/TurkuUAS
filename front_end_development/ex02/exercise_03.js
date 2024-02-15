const convertToMinutesFormat = hoursInHundredths => {
 
    let list = hoursInHundredths.split(".");
    let hours = Number(list[0]);
    let minutes = Number(list[1]) * 0.6;
    let totalMinutes = (hours * 60) + minutes;

    let formattedHours = Math.floor(totalMinutes / 60);
    let formattedMinutes = totalMinutes % 60;

    if (formattedHours < 10) {
        formattedHours = "0" + formattedHours;
    }
    if (formattedMinutes < 10) {
        formattedMinutes = "0" + formattedMinutes;
    }

    return `${formattedHours}:${formattedMinutes}`;
}

function displayResult(time, timeInput) {
    var resultDiv = document.getElementById('result');
    if (time) {
        resultDiv.textContent = timeInput + " hours are in hours and minutes equal to: " + time;
    } else {
        resultDiv.textContent = "Please enter a valid time!";
    }
}

function checkTime() {
    var timeInput = document.getElementById('timeInput').value;
    var time = timeInput;
    if (!isNaN(time)) {
        var time = convertToMinutesFormat(time, timeInput);
        displayResult(time, timeInput);
    } else {
        alert("Please enter a valid time!");
    }
}

function isLeapYear(year) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        return true;
    }
    else {
        return false;
    }
}

console.log(isLeapYear(2020));
console.log(isLeapYear(2021));
console.log(isLeapYear(2024));
console.log(isLeapYear(2100));
console.log(isLeapYear(2004));
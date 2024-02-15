function getRandomIntegerFromRange(startRange, endRange) {
    return Math.floor(Math.random() * (endRange - startRange + 1)) + startRange;
}

console.log(getRandomIntegerFromRange(1, 10));
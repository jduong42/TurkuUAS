const distances = [164, 526, 248, 12, 81, 181, 34]
let sum = 0;

for (let i = 0; i < distances.length; i++) {
    sum = sum + distances[i];
}

console.log(sum);

let x = 0;
let y = 0;

while (distances.length > x) {

    y = y + distances[x];
    x++;

}

console.log(y);
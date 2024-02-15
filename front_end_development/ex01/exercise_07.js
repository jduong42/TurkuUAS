const points = [64, 56, 48, 12, 81, 91, 34, 19, 95, 55];
const filtered_points = points.filter(check_filter);
const grades = points.map(point => {
    if (point >= 85) {
        return 5;
    } else if (point >= 70) {
        return 4;
    } else if (point >= 60) {
        return 3;
    } else if (point >= 50) {
        return 2;
    } else if (point >= 40) {
        return 1;
    } else {
        return 0;
    }
})

const sum = points.reduce((acc, point) => acc + point, 0)
const average_grade = sum / points.length;

function check_filter(points) {
    return points >= 40;
}

console.log(filtered_points);
console.log(grades);
console.log(average_grade);

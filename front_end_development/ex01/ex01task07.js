debugger;

const points = [64, 56, 48, 12, 81, 91, 34, 19, 95, 55];

points.splice(8, 1);                        // 95 is removed

/*
points = points.filter(function(aPoint) {
    return aPoint >= 40;
});
*/                                          // TypeError: Assignment to constant variable.<-- const points


const enough_points = points.filter(function(aPoint) {
    return aPoint >= 40;
});


enough_points.sort();

document.getElementById('displayarea').innerText = enough_points;
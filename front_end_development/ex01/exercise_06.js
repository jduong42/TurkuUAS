const distances = [ 164, 526, 248, 12, 81, 181, 34 ];

function len_distance(distances) {
    return distances.length;
}

function add_distance(distances) {
    distances.push(8, 533, 76);
    return distances;
}

function remove_distance(distances) {
    const index = distances.indexOf(248);
    distances.splice(index, 1);
    return distances;
}

const distances_duplicate = [...distances];

console.log(len_distance(distances));
console.log(add_distance(distances));
console.log(remove_distance(distances));
console.log(distances_duplicate);

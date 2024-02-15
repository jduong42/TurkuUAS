// Task 3 example of for in loop

const person = {name: "John", age: 30 };

for (let key in person) {
    console.log(`${key}: ${person[key]}`);
}

// Task 3 example of object entries method

console.log(Object.entries(person)[0]); 

// Returns only name and John, because its the first key value -pair in the object

// Task 3 example of object keys method

console.log(Object.keys(person));

// Returns name and age as an array of strings

// Task 3 example of object values method

console.log(Object.values(person));

// Returns John and 30 as an array of strings

const musician = {
    name: "Sting",
    realName: 'Gordon Matthew Thomas Sumner',
    instrument: {
        type: "bass"
    }
};

for (let key in musician) {
    console.log(`${key}: ${musician[key]}`);
}

const musician_2 = [
    {name: "Sting", realName: 'Gordon Matthew Thomas Sumner', instrument: {type: "bass"}},
    {name: "the Kid Laroi", realName: 'Charlton Kenneth Jeffrey Howard', instrument: {type: "vocals"}}
];

console.log(Object.entries(musician_2)[1]);
console.log(Object.keys(musician_2[1]));
console.log(Object.values(musician_2[1]));
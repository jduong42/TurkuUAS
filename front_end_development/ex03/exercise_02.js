const musician = {
    name: "Sting",
    realName: 'Gordon Matthew Thomas Sumner',
    instrument: {
        type: "bass"
    }
};

// Read the attributes name and instrument into the variables name and instrument.

const {name, instrument} = musician;

console.log(name);
console.log(instrument);

const {name: nameOfArtist, instrument: instrumentOfArtist} = musician;

console.log(nameOfArtist);
console.log(instrumentOfArtist);

const {instrument: {type: instrumentTypeOfArtist}} = musician;

console.log(instrumentTypeOfArtist);

const {instrument: {make: instrumentMakeOfArtist = "unknown"}} = musician;

console.log(instrumentMakeOfArtist);
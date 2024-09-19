var songlist = ["Keep Up", "Timanttei", "Big Dagws", "Run away", "Astra", "Fe!n"]

function pickRandomSong() {
    var randomIndex = Math.floor(Math.random() * songlist.length);
    return songlist[randomIndex];
}

console.log(pickRandomSong());
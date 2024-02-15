const song = {
    name: "Stay",

    get duration() {
        return this._duration;
    },

    set duration(newDuration) {
        this._duration = newDuration;
    }
}

song.duration = "3:30";
console.log(song.duration);
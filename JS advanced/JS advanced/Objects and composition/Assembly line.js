function createAssemblyLine(){
    const obj = {
        hasClima: function(param){
            param['temp'] = 21,
            param['tempSettings'] = 21,
            param['adjustTemp'] = function(){
                if (this.temp < this.tempSettings){this.temp += 1}
                else if (this.temp > this.tempSettings){this.temp -= 1}
            }
        },
        hasAudio: function(param){
            param['currentTrack'] = {name: null, artist: null},
            param['nowPlaying'] = function(){if(this.currentTrack != null){console.log(`Now playing '${this.currentTrack.name}' by ${this.currentTrack.artist}`)}}
        },
        hasParktronic: function(param){
            param['checkDistance'] = function(dist){
                let dist_num = parseFloat(dist);
                if (dist_num < 0.1){console.log("Beep! Beep! Beep!")}
                else if (dist_num >= 0.1 && dist_num < 0.25){console.log("Beep! Beep!")}
                else if (dist_num >= 0.25 && dist_num < 0.5){console.log("Beep!")}
                else{console.log('')}
            }
        }
    }
    return obj
};
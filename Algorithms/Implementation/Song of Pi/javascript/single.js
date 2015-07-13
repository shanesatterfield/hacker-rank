var readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

// The number of test cases to read.
var T = -1;

// The test cases.
var lines = [];

rl.on('line', function(line) {
    if( T <= 0 ) {
        T = parseInt( line );
    }
    else if( lines.length < T ) {
        lines.push( line );

        if( lines.length == T ) {
            main();
            rl.close();
        }
    }
    else {
        rl.close();
    }
})

function main() {
    for( var i in lines ) {
        if( song.isPiSong( lines[i] ) == true ) {
            console.log("It's a pi song.");
        }
        else {
            console.log("It's not a pi song.");
        }
    }
}

var song = {
    MY_PI: '31415926535897932384626433833',

    isPiSong: function( song ) {
        var words  = getWords( song );
        var result = true;

        for( var i = 0; i < words.length; ++i ) {
            if( words[i].length != parseInt( this.MY_PI[i] ) ) {
                result = false;
                break;
            }
        }

        return result;
    }
};

function getWords( text ) {
    return text.split(/\W+/);
}

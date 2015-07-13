var readline = require('readline');
var song = require('./song');

// Sets up reading from stdin.
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

// The number of test cases to read.
var T = -1;

// The test cases.
var lines = [];

// Processes stdin.
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

// Takes the input and prints the proper output to stdout.
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

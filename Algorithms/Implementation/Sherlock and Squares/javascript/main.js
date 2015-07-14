var readline = require('readline');
var squares = require('./squares');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

var T = -1;
var lines = [];

rl.on('line', function( line ) {
    if( T < 0 ) {
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
});

function main() {
    for( var i in lines ) {
        var interval = lines[i].split(/[^0-9]+/);
        console.log( squares.squaresInterval( parseInt(interval[0]), parseInt(interval[1]) ) );
    }
}

var readline = require('readline');
var squares = {
    squaresInterval: function( a, b ) {
        var count = 0;
        if( this.isSquare(a) ) {
            count++;
        }
        count += Math.floor(Math.sqrt( b )) - Math.floor(Math.sqrt( a ));
        return count;
    },

    isSquare: function( num ) {
        return Math.pow( Math.floor(Math.sqrt(num)), 2 ) == num;
    }
};

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

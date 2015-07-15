function main() {
    for( var i in lines ) {
        var interval = lines[i].split(/[^0-9]+/);
        console.log( squares.squaresInterval( parseInt(interval[0]), parseInt(interval[1]) ) );
    }
}

var squares = module.exports = {
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
}

process.stdin.resume();
process.stdin.setEncoding('ascii');

var T = -1;
var lines = [];

process.stdin.on('data', function( data ) {
    data = data.split('\n');

    if( T <= 0 ) {
        T = parseInt( data[0] );
    }

    for( var i = 1; i <= T; ++i ) {
        if( data[i].length > 0 ) {
            lines.push( data[i] );
        }
    }
});

process.stdin.on('end', function() {
    main();
})

var exports = module.exports = {
    fib: function( N ) {
        var total = 0;
        var curr = 1;
        var prev = 1;

        while( curr <= N ) {
            if( curr % 2 == 0 ) {
                total += curr;
            }

            curr += prev;
            prev = curr - prev;
        }

        return total;
    }
}

function main() {
    for( var i in lines ) {
        console.log( exports.fib( parseInt( lines[i] ) ) );
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
        lines.push( data[i] );
    }
});

process.stdin.on('end', function() {
    main();
});

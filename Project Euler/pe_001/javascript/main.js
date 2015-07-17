var exports = module.exports = {
    // Does not work for the 10^9 edge case because Javascript cannot handle numbers that large.
    // It works for every case less than that one though. I'll implement something to get around
    // that though.
    fizzbuzz: function( num ) {
        N = num-1;
        return this.calcFizz( N, 3 )- this.calcFizz( N, 15 ) + this.calcFizz( N, 5 );
    },

    calcFizz: function( N, K ) {
        return this.fastSum( Math.floor(N/K) ) * K;
    },

    fastSum: function( N ) {
        var total = Math.floor(N/2) * (N+1);
        if( N % 2 != 0 ) {
            total += Math.floor((N+1) / 2);
        }
        return total;
    }
}

function main() {
    for( var i in lines ) {
        console.log( exports.fizzbuzz( parseInt(lines[i]) ) );
    }
}

process.stdin.resume();
process.stdin.setEncoding('ascii');

var T = -1;
var lines = [];

process.stdin.on('data', function( data ) {
    data = data.split('\n');
    if( T <= 0 ) {
        T = parseInt( data[0] )
    }

    for( var i = 1; i <= T; ++i ) {
        lines.push( data[i] );
    }
});

process.stdin.on('end', function() {
    main();
});

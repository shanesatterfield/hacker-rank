function main() {
    for( var i in lines ) {
        console.log(beast.getDecent(parseInt( lines[i] )));
    }
}

var beast = module.exports = {
    getDecent: function( N ) {
        var original = N;
        var fives = 0;
        var threes = 0;

        if( N < 3 ) {
            return -1;
        }

        fives = Math.floor( N / 3 );
        N %= 3;

        threes = Math.floor( N / 5 );
        N %= 5;

        while( N > 0 && fives > 0 && N <= original ) {
            N += 3;
            fives -= 1;

            if( N % 5 == 0 ) {
                threes += Math.floor( N / 5 );
                N %= 5;
            }
        }

        if( (fives <= 0 && threes <= 0) || N > 0) {
            return -1;
        }

        return parseInt([this.repeatString('555', fives), this.repeatString('33333', threes)].join(''));
    },

    repeatString: function( string, count ) {
        list = [];

        for( var i = 0; i < count; ++i ) {
            list.push( string );
        }

        return list.join('');
    }
}

var T = -1;
var lines = [];

process.stdin.resume();
process.stdin.setEncoding('ascii');

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

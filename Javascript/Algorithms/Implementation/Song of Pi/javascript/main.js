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

var song = module.exports = {
    // This is the value of pi that will be used for the purposes of this problem.
    MY_PI: '31415926535897932384626433833',

    // Determines if the string is a pie song.
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

// Function to get a list of words from a string.
function getWords( text ) {
    return text.split(/\W+/);
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
});

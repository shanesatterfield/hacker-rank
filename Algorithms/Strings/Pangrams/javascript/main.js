/*
Pangrams
========
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.
*/
var exports = module.exports = {
    isPangram: function( sentence ) {
        var newSentence = sentence.toLowerCase().replace(/[^a-z]+/g, '');
        var letters = {};
        for( var i in newSentence ) {
            letters[ newSentence[i] ] = ( letters[newSentence[i]] || 0 ) + 1;
        }
        return Object.keys( letters ).length == 26;
    }
};

function main() {
    if( exports.isPangram( text ) ) {
        console.log('pangram');
    }
    else {
        console.log('not pangram');
    }
}

process.stdin.resume();
process.stdin.setEncoding('ascii');

var text = '';
process.stdin.on('data', function( data ) {
    text = data;
});

process.stdin.on('end', function() {
    main();
});

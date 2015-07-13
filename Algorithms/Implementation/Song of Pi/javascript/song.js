module.exports = {
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

module.exports = {
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

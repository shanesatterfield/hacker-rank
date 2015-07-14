var assert = require('assert');
var squares = require('./squares');

describe('Sherlock and Squares', function() {
    it('Test Case 1', function() {
        assert.equal( squares.squaresInterval(  3,  9 ), 2 );
        assert.equal( squares.squaresInterval( 17, 24 ), 0 );
    });

    it('Should inclusive', function() {
        assert.equal( squares.squaresInterval( 2, 2 ), 0 );
        assert.equal( squares.squaresInterval( 3, 3 ), 0 );
        assert.equal( squares.squaresInterval( 4, 4 ), 1 );
        assert.equal( squares.squaresInterval( 9, 9 ), 1 );
    });

    it('Should count properly between two squares', function() {
        assert.equal( squares.squaresInterval( 4,  9 ), 2 );
        assert.equal( squares.squaresInterval( 4, 16 ), 3 );
    });

    it('Should correctly find squares', function() {
        assert.equal( squares.isSquare(  2 ), false );
        assert.equal( squares.isSquare(  3 ), false );
        assert.equal( squares.isSquare(  4 ), true  );
        assert.equal( squares.isSquare(  5 ), false );
        assert.equal( squares.isSquare(  9 ), true  );
        assert.equal( squares.isSquare( 10 ), false );
        assert.equal( squares.isSquare( 11 ), false );
        assert.equal( squares.isSquare( 12 ), false );
        assert.equal( squares.isSquare( 16 ), true  );
    });
});

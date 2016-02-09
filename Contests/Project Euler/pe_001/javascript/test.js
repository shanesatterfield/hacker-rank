var assert = require('assert');
var fizz = require('./main');

describe('pe_001', function() {
    it('Test Case 1', function() {
        assert.equal( fizz.fizzbuzz(10), 23 );
    });

    it('Test Case 2', function() {
        assert.equal( fizz.fizzbuzz(100), 2318 );
    });

    it('Edge Case Large', function() {
        //assert.equal( fizz.fizzbuzz( 1000000000 ), 233333333166666668 );
        assert.equal( fizz.fizzbuzz( 999999999 ), 233333332166666669 );
    });

    it('Edge Case Small', function() {
        assert.equal( fizz.fizzbuzz( 1 ), 0 );
    });
});

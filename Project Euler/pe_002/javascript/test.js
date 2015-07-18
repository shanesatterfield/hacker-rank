var assert = require('assert');
var fib = require('./main');

describe('pe_002', function() {
    it('Test Case 1', function() {
        assert.equal( fib.fib(10), 10 );
    });

    it('Test Case 2', function() {
        assert.equal( fib.fib(100), 44 );
    });

    it('should not crash on edge case', function() {
        assert( fib.fib( 4 * Math.pow(10, 16) ) );
    })
});

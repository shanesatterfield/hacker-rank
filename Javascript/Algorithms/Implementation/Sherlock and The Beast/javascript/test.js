var assert = require('assert');
var beast = require('./main');

describe('Sherlock and The Beast', function() {
    it('Test Case 1', function() {
        assert.equal(beast.getDecent(  1 ), -1);
        assert.equal(beast.getDecent(  3 ), 555);
        assert.equal(beast.getDecent(  5 ), 33333);
        assert.equal(beast.getDecent( 11 ), 55555533333);
        assert.equal(beast.getDecent( 14 ), 55555555533333);
        assert.equal(beast.getDecent( 16 ), 5555553333333333);
    });

    it('should repeat string properly', function() {
        assert.equal(beast.repeatString('555', 3), '555555555');
        assert.equal(beast.repeatString('asdf', 2), 'asdfasdf');
    });

    it('should not care about types', function() {
        assert.equal(beast.repeatString(555, 3), '555555555');
        assert.equal(beast.repeatString(-1, 2), '-1-1');
    });
});

var assert = require('assert')
var tiles  = require('./main');
var delta  = 0.0001;

describe('Sherlock and Moving Tiles', function() {
    it('Test Case 1', function() {
        var expected = 4.1421;
        var actual = tiles.getTime(10, 1, 2, 50);
        assert(actual >= expected - delta || actual <= expect + delta);
    })

    it('Test Case 2', function() {
        var expected = 0;
        var actual = tiles.getTime(10, 1, 2, 100);
        assert(actual >= expected - delta || actual <= expect + delta);
    })
})

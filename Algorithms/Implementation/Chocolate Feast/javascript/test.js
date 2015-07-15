var assert = require('assert')
var feast = require('./main')

describe('Chocolate Feast', function() {
    it('Test Case 1', function() {
        assert.equal( feast.feast(10, 2, 5), 6 )
        assert.equal( feast.feast(12, 4, 4), 3 )
        assert.equal( feast.feast( 6, 2, 2), 5 )
    })
})

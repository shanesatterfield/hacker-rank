var assert = require('assert');
var pangram = require('./main');

describe('Pangrams', function() {
    it('Test Case 1', function() {
        assert.equal(pangram.isPangram('We promptly judged antique ivory buckles for the next prize'), true)
    });

    it('Test Case 2', function() {
        assert.equal(pangram.isPangram('We promptly judged antique ivory buckles for the prize'), false);
    });

    it('should be case insensitive', function() {

        assert.equal(pangram.isPangram('We promptly judged antique ivory buckles for the next prize'), true)
        assert.equal(pangram.isPangram('WE PROMPTLY JUDGED ANTIQUE IVORY BUCKLES FOR THE NEXT PRIZE'), true);

        assert.equal(pangram.isPangram('WE PROMPTLY JUDGED ANTIQUE IVORY BUCKLES FOR THE PRIZE'), false);
        assert.equal(pangram.isPangram('We promptly judged antique ivory buckles for the prize'), false);
    });
});

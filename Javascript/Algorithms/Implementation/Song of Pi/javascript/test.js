var assert = require('assert');
var song = require('./main.js');

describe('Song of Pi', function() {
    it('Test Case 1', function() {
        assert.equal(song.isPiSong("Can I have a large container of coffee right now"), true);
        assert.equal(song.isPiSong("Can I have a large container of tea right now"), false);
        assert.equal(song.isPiSong('Now I wish I could recollect pi Eureka cried the great inventor Christmas Pudding Christmas Pie Is the problems very center'), true);
    });

    it('Test Case 2', function() {
        assert.equal(song.isPiSong("How I need a drink alcoholic in nature after the tough chapters involving quantum mechanics"), true);
        assert.equal(song.isPiSong("How I wish I could recollect pi easily today"), true);
        assert.equal(song.isPiSong("Hello world"), false);
        assert.equal(song.isPiSong("May I have a large container of coffee cream and sugar"), true);
        assert.equal(song.isPiSong("May I have a large container of coffee cream and sugar and cake"), false);
    });
});

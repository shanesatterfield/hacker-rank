assert   = require 'assert'
sherlock = require '../src/main'

describe 'Sherlock and Valid String', ->
    it 'should work with one at end', ->
        assert.equal(true,  sherlock.sherlock('aaabbbc'))

    it 'should work with one at beginning', ->
        assert.equal(true,  sherlock.sherlock('abbcc'))

    it 'should work with two at end', ->
        assert.equal(false, sherlock.sherlock('aabbcd'))

    it 'should work with two at beginning', ->
        assert.equal(false, sherlock.sherlock('cdaabb'))

    it 'should work with one at middle', ->
        assert.equal(true,  sherlock.sherlock('aabdbcc'))

    it 'should work with two at middle', ->
        assert.equal(false, sherlock.sherlock('aabdebcc'))

    it 'should work with works with space', ->
        assert.equal(true,  sherlock.sherlock('a abdbcc '))

    it 'should fail with invalid spaces', ->
        assert.equal(false, sherlock.sherlock('aabdbcc '))

    it 'should remove additional ones', ->
        assert.equal(true,  sherlock.sherlock('aaabbbcccc'))

    it 'Test Case 2', ->
        assert.equal(true, sherlock.sherlock('jtqgugmcsxvdwidtcyqpogkdifapuloqykjfxruvfrshcehekoiwbpbrprahwvhliglyxynjotbaswnnnmxbkmcftvsdqajemeul'))

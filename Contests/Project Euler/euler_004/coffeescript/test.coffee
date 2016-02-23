assert = require 'assert'
main   = require './main'

describe 'Project Euler #4: Largest palindrome product', ->
    it 'test case 1', ->
        assert.equal main.pe_004(101110), 101101

    it 'test case 2', ->
        assert.equal main.pe_004(800000), 793397

exports = module.exports =
    palindromes: []
    pe_004: (num) ->
        if this.palindromes.length == 0
            this.findPalindromes()

        curr = this.palindromes[0]
        for n in this.palindromes
            if n < num
                curr = n
            else
                break
        return curr


    findPalindromes: (start = 100, stop = 999) ->
        for i in [start..stop]
            for j in [start..stop]
                temp = i * j
                this.palindromes.push temp if this.isPalindrome temp

        this.palindromes.sort()

    isPalindrome: (num) ->
        num = num.toString() if typeof num is 'number'
        len = num.length
        if len isnt 6
            return false

        for i in [0..Math.floor(len/2)-1]
            return false if num[i] isnt num[len-i-1]
        return true

console.log(exports.pe_004(101110))

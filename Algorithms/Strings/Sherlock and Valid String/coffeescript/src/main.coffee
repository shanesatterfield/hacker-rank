# Sherlock and Valid String

exports.sherlock = (string) ->
    arr       = ( v for k, v of count(string) ).sort (x,y) -> x-y
    max_count = 1
    i         = 0
    j         = arr.length - 1

    while i < j and arr[i] != arr[j] and max_count >= 0
        diff = Math.abs(arr[i] - arr[j])

        if diff >= max_count and arr[i] == 1
            max_count -= 1
            i += 1

        else
            max_count -= diff
            i++
            j--

    return max_count >= 0

count = (arr) ->
    counter = {}

    for n in arr
        if n not of counter
            counter[n] = 0
        counter[n] += 1

    return counter

sherlockTranslate = (bool) ->
    return "YES" if     bool
    return "NO"


# IO Handling #

readline = require 'readline'

rl = readline.createInterface({
  input:    process.stdin,
  output:   process.stdout,
  terminal: false
})

rl.on 'line', (line) ->
    console.log sherlockTranslate exports.sherlock line

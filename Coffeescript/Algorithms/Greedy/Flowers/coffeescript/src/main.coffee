Array.prototype.sum = () ->
    return 0 if this.length is 0
    return this.reduce (x,y) -> x+y

exports.flowers = (k, arr) ->
    prices = arr.sort (x,y) -> y-x
    result = 0
    for i in [0..(prices.length)//k]
        result += (i+1) * prices.splice(0,k).sum()
    return result


# IO Handling #

process.stdin.resume()
process.stdin.setEncoding('ascii')

t = k = -1
lines = []

process.stdin.on 'data', (data) ->
    data = data.split '\n'

    lines = data.map (d) -> d.split(/\W+/).map (x) -> parseInt x
    t = lines[0][0]
    k = lines[0][1]

process.stdin.on 'end', ->
    console.log exports.flowers k, lines[1]

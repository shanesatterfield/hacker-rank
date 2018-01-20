function processData(input) {
    var L, s1, s2, query_num, queries;
    // line = input.split()
    lines = input.trim().split('\n')

    line = lines[0].split(' ')
    L    = line[0];
    s1   = line[1];
    s2   = line[2];

    query_num  = Math.floor(lines[1])
    queries    = lines.slice(2)
    for( var i = 0; i < query_num; ++i ) {
        console.log(tiles.getTime(L, s1, s2, queries[i]))
    }
}

var tiles = module.exports = {
    getTime: function( L, s1, s2, Q ) {
        return Math.sqrt(2) * (L - Math.sqrt(Q)) / Math.abs(s2 - s1);
    }
};


process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});

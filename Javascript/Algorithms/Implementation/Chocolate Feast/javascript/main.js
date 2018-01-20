function main() {
    for( var i in lines ) {
        var args = lines[i].split(' ').map(function( x ) { return parseInt(x); });
        console.log(exports.feast( args[0], args[1], args[2] ));
    }
}

var exports = module.exports = {
  feast: function( N, C, M ) {
      var count = 0;
      var temp_count = Math.floor( N / C );
      while( true ) {
          var free_choco = temp_count + (count % M);
          count += temp_count;

          if( free_choco < M ) {
              break;
          }

          temp_count = Math.floor(free_choco / M);
      }

      return count;
  }
}

process.stdin.resume();
process.stdin.setEncoding('ascii');

var T = -1;
var lines = [];

process.stdin.on('data', function( data ) {
    data = data.split('\n');

    if( T <= 0 ) {
        T = parseInt( data[0] );
    }

    for( var i = 1; i <= T; ++i ) {
        if( data[i].length > 0 ) {
            lines.push( data[i] );
        }
    }
});

process.stdin.on('end', function() {
    main();
});

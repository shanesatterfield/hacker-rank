processData = (input) ->
    console.log input

process.stdin.resume();
process.stdin.setEncoding("ascii");

_input = "";
process.stdin.on "data", (input) ->
    _input += input;

process.stdin.on "end", ->
   processData _input

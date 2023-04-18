var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split(' ');

let a = parseInt(lines.shift());
let b = parseInt(lines.shift());

if (a%b == 0 || b%a == 0)
    console.log('Sao Multiplos')
else
    console.log('Nao sao Multiplos')
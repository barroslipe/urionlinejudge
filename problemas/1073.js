var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let n = parseInt(lines.shift());

for(let i=2;i<=n;i = i+2){
    console.log(i + '^2 = ' + (i * i))
}
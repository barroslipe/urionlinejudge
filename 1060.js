var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let contador= 0;

for(let i=0;i<6;i++){
    let a = parseFloat(lines.shift());
    if(a > 0) 
        contador++;
}

console.log(contador +' valores positivos');
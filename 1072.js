var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let n = parseInt(lines.shift())

let contador = 0;

for(let i=0; i<n; i++){
    let x = parseInt(lines.shift())

    if( x >= 10 && x <= 20){
        contador++;
    }
}

console.log(contador + ' in');
console.log(Math.abs(contador - n) + ' out');
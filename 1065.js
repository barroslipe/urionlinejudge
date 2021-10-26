var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let contador = 0;
for(let i=0; i< 5; i++){
    let n = parseInt(lines.shift());

    if(n%2 == 0)
        contador++;
}

console.log(contador + ' valores pares');
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let contador = 0, soma = 0;

for(let i=0; i<6; i++){
    let n = parseFloat(lines.shift())

    if(n > 0){
        contador++;
        soma += n;
    }
}

console.log(contador + ' valores positivos');
console.log((soma/contador).toFixed(1));
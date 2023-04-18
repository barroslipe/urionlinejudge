var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entrada = lines.shift().split(' ').map(Number);

m = entrada[0];
n = entrada[1];

while((m > 0) && (n > 0)) {

    let aux;
    if( m > n){
        aux = n;
        n = m;
        m = aux;
    }
    
    let soma = 0;
    for(let i=m; i<=n; i++){
        process.stdout.write(i + ' ');
        soma += i;
    }
    console.log('Sum='+soma);

    entrada = lines.shift().split(' ').map(Number);

    m = entrada[0];
    n = entrada[1];
}
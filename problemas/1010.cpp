#include <iostream>
#include <iomanip>  
 
using namespace std;

struct peca {
    int nome;
    int quantidade;
    float valor;
} peca1, peca2;


int main() {

    float total;

    cin >> peca1.nome >> peca1.quantidade >> peca1.valor;
    cin >> peca2.nome >> peca2.quantidade >> peca2.valor;

    total = peca1.quantidade*peca1.valor + peca2.quantidade*peca2.valor;

    cout << fixed << setprecision(2) << "VALOR A PAGAR: R$ "<< total << "\n";
 
    return 0;
}
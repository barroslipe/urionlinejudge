#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
	
	double dinheiro;

	cin >> dinheiro;
	
	cout << "NOTAS:\n";
	
	int notas[6] = {100, 50, 20, 10, 5, 2};
	for(int i=0; i<6; i++) {
		
		int quantidade_notas = dinheiro/notas[i];
		dinheiro -= quantidade_notas*notas[i];

		cout << quantidade_notas << " nota(s) de R$ " << fixed << setprecision(2) << (float)notas[i] << "\n";

	}
	cout << "MOEDAS:\n";

	dinheiro += 0.001;

	float moedas[6] = {1.00, 0.50, 0.25, 0.10, 0.05, 0.01};
	for(int i=0; i<6; i++){

		int quantidade_moedas = dinheiro/moedas[i];
		dinheiro -= quantidade_moedas*moedas[i];
		
		cout << quantidade_moedas << " moeda(s) de R$ " << moedas[i] << "\n";
	}

	return 0;
}

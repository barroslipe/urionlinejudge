#include <iostream>
 
using namespace std;
 
int main() {

    int hora_inicial, minuto_inicial, hora_final, minuto_final, tempo_inicial, tempo_final, tempo_decorrido;

    cin >> hora_inicial >> minuto_inicial >> hora_final >> minuto_final;

    tempo_inicial = 60*hora_inicial + minuto_inicial;
    tempo_final = 60*hora_final + minuto_final;

    if (tempo_final <= tempo_inicial)
        tempo_final += 24*60;
        
    tempo_decorrido = tempo_final - tempo_inicial;


    cout << "O JOGO DUROU " << tempo_decorrido/60 << " HORA(S) E " << tempo_decorrido%60 << " MINUTO(S)\n";

    return 0;
}
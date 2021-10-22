#include <iostream>
#include <iomanip>  
 
using namespace std;
 
int main() {

    int id, horas;
    float grana;

    cin >> id >> horas >> grana;

    cout << "NUMBER = "<< id << "\n";
    cout << fixed << setprecision(2) << "SALARY = U$ "<< grana*horas << "\n";
 
    return 0;
}
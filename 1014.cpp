#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
 
    int x;
    double y, consumo;

    cin >> x >> y;

    consumo = x / y;

    cout << fixed << setprecision(3) << consumo << " km/l" << "\n";

    return 0;
}
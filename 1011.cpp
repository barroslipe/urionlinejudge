#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
 
    const double PI = 3.14159;
    double raio, area;

    cin >> raio;

    area =  4.0/3 * PI * raio * raio * raio;

    cout << fixed << setprecision(3) << "VOLUME = " << area << "\n";
 
    return 0;
}
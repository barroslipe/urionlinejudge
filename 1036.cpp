#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;
 
int main() {
	
	double a, b, c, delta, x1, x2;

	cin >> a >> b >> c;

	if ( a == 0 ) 
		cout << "Impossivel calcular\n";
	else {

		delta = b * b - 4 * a * c;

		if( delta < 0) 
			cout << "Impossivel calcular\n";
		else {

			x1 = ((- b) + sqrt(delta)) / (2 * a);
			x2 = ((- b) - sqrt(delta)) / (2 * a);
	
			cout << fixed << setprecision(5);
	
			cout << "R1 = " << x1 << "\n";
			cout << "R2 = " << x2 << "\n";
		}

	}

	return 0;
}

#include <iostream>
#include <iomanip>

using namespace std;
 
int main() {

	float a, b, media;

	cin >> a >> b;

	media = (a * 3.5 + b * 7.5) / 11;

	cout << fixed << setprecision(5) << "MEDIA = "<< media << "\n";

	return 0;
}

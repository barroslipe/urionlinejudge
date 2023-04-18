#include <iostream>
 
using namespace std;
 
int main() {
 
    int a, b, r, q;

    cin >> a >> b;

    q = a/b;

    if ( a < 0 && b > 0 && a%b != 0) {
        q -= 1;
    }else if(a < 0 && b < 0 && a%b != 0) {
        q += 1;
    }

    r = a - b*q;

    cout << q << " " << r << "\n";

    return 0;
}
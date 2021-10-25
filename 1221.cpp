#include <iostream>
#include <math.h>
 
using namespace std;
 
int main() {
 
    int n, x;
    bool prime;

    cin >> n;

    for(int i=0;i<n;i++){
        cin >> x;
        prime=true;



        for(int j=2;j<=sqrt(x);j++){
            if(x%j == 0) {
                cout << "Not Prime\n";
                prime = false;
                break;
            }
        }
        if(prime) cout << "Prime\n";
    }
 
    return 0;
}
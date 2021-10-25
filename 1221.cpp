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
        
        if(x == 1 || x == 2)
            cout << "Prime\n";
        else if(x % 2 == 0)
            cout << "Not Prime\n";
        else{
            for(int j=3;j<=sqrt(x);j+=2){
                if(x%j == 0) {
                    cout << "Not Prime\n";
                    prime = false;
                    break;
                }
            }
            if(prime) cout << "Prime\n";
        }
    }
 
    return 0;
}
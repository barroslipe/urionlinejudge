#include <iostream>
 
using namespace std;
 
int main() {
 
    int h, z, l;

    string nome;

    cin >> h >> z >> l;


    if(h > z) {
        if(h < l)
            nome ="huguinho";
        else if(l > z)
            nome = "luisinho";
        else
            nome = "zezinho";
    }else if(z < l){
        nome ="zezinho";
    }else if(l > h)
        nome = "luisinho";
    else
        nome ="huguinho";

    cout << nome << "\n";

    return 0;
}
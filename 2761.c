#include <stdio.h>

int main(){

    int a;
    float b;
    char c;
    char frase[50];


    scanf("%d %f %c %[^\n]", &a, &b, &c, frase);

    printf("%d%.6f%c%s\n", a, b, c, frase);
    printf("%d\t%.6f\t%c\t%s\n", a, b, c, frase);
    printf("%10d%10.6f%10c%10s\n", a, b, c, frase);

    return 0;
}
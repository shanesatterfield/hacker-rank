#include <stdio.h>
#include <stdlib.h>

int main( int argc, char* argv[] ) {
    int n1 = 0;
    long n2 = 0;
    long long n3 = 0;
    char n4 = ' ';
    float n5 = 0.f;
    double n6 = 0.f;
    scanf("%d %ld %lld %c %f %lf", &n1, &n2, &n3, &n4, &n5, &n6);
    printf("%d\n%ld\n%lld\n%c\n%f\n%lf\n", n1, n2, n3, n4, n5, n6);
    return 0;
}

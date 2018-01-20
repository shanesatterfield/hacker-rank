#include <iostream>
#include <math.h>

int closest( int a, int b, int x );

int main(int argc, char* argv[]) {
    int T, a, b, x;
    std::cin >> T;

    for( int i = 0; i < T; ++i ) {
        std::cin >> a >> b >> x;
        std::cout << closest( a, b, x ) << std::endl;
    }

    return 0;
}

int closest( int a, int b, int x ) {
    return int(round(pow(a, b) / float(x))) * x;
}

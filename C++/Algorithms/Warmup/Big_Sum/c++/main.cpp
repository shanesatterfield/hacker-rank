#include <iostream>

int main( int argc, char* argv[] ) {
    int T;
    long long sum, temp;

    std::cin >> T;
    for( int i = 0; i < T; ++i ) {
        std::cin >> temp;
        sum += temp;
    }

    std::cout << sum << std::endl;
    return 0;
}

#include <iostream>

int main( int argc, char* argv[] )
{
    int T, socks;
    std::cin >> T;
    for( int i = 0; i < T; ++i )
    {
        std::cin >> socks;
        std::cout << (socks+1) << std::endl;
    }
    return 0;
}

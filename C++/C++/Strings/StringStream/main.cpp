#include <iostream>
#include <sstream>
#include <vector>

std::vector<int> parseIntegers();

int main( int argc, char* argv[] ) {
    std::vector<int> vec = parseIntegers();
    for( int i = 0; i < vec.size(); ++i ) {
        std::cout << vec[i] << std::endl;
    }
    return 0;
}

std::vector<int> parseIntegers() {
    std::vector<int> vec;
    int num;
    char temp;

    while( std::cin >> num ) {
        std::cin >> temp;
        vec.push_back( num );
    }

    return vec;
}

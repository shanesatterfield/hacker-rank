#include <iostream>

std::string words[] = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
};

int main( int argc, char* argv[] ) {
    int SIZE = sizeof(words)/sizeof(words[0]);
    int a, b;
    if( std::cin >> a >> b ) {
        for( int i = a; i <= b; ++i ) {
            if( i >= 1 && i <= 9) {
                std::cout << words[i-1] << std::endl;
            }
            else {
                std::cout << (( i % 2 == 0 )? "even" : "odd") << std::endl;
            }
        }
    }
    return 0;
}

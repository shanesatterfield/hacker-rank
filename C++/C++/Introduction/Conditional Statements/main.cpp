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
    int num = 0;
    int SIZE = sizeof(words)/sizeof(words[0]);

    while( std::cin >> num ) {
        if( num <= SIZE && num >= 1 ) {
            std::cout << words[num-1] << std::endl;
        }
        else {
            std::cout << "Greater than 9" << std::endl;
        }
    }
    return 0;
}

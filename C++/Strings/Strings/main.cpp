#include <iostream>

int main( int argc, char* argv[] ) {
    std::string s1 = "";
    std::string s2 = "";

    if( std::cin >> s1 >> s2 ) {
        std::cout << s1.size() << " " << s2.size() << std::endl;
        std::cout << (s1 + s2) << std::endl;

        char temp = ' ';
        temp = s2[0];
        s2[0] = s1[0];
        s1[0] = temp;
        std::cout << s1 << " " << s2 << std::endl;
    }

    return 0;
}

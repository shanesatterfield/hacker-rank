#include <iostream>
#include <vector>

void printVector( std::vector<int> &vec );

int main( int argc, char* argv[] )
{
    int T, temp, temp2;
    std::vector<int> vec;

    std::cin >> T;
    for( int i = 0; i < T; ++i ) {
        std::cin >> temp;
        vec.push_back( temp );
    }

    std::cin >> temp;
    vec.erase( vec.begin()+(temp-1) );

    std::cin >> temp >> temp2;
    vec.erase( vec.begin()+(temp-1), vec.begin()+(temp2-1) );

    printVector( vec );
    return 0;
}

void printVector( std::vector<int> &vec ) {
    std::cout << vec.size() << std::endl;
    for( int i = 0; i < vec.size(); ++i ) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
}

#include <iostream>
#include <vector>
#include <algorithm>

int main( int argc, char* argv[] )
{
    int T, temp;
    std::vector<int> vec;

    if( std::cin >> T )
    {
        for( int i = 0; i < T && std::cin >> temp; ++i )
        {
            vec.push_back( temp );
        }
    }

    sort( vec.begin(), vec.end() );
    for( int i = 0; i < vec.size(); ++i )
    {
        std::cout << vec[i] << ' ';
    }
    std::cout << std::endl;

    return 0;
}

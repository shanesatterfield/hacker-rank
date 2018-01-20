#include <iostream>
#include <vector>

int main( int argc, char* argv[] ) {
    int T, temp, ans;
    std::vector<int> vec;
    std::vector<int>::iterator iter;

    std::cin >> T;
    for( int i = 0; i < T; ++i ) {
        std::cin >> temp;
        vec.push_back( temp );
    }

    std::cin >> T;
    for( int i = 0; i < T; ++i ) {
        std::cin >> temp;
        iter = std::lower_bound( vec.begin(), vec.end(), temp );
        ans = std::distance(vec.begin(), iter);
        
        if( vec[ans] == temp ) {
            std::cout << "Yes ";
        }
        else {
            std::cout << "No ";
        }

        std::cout << (ans+1) << std::endl;
    }

    return 0;
}

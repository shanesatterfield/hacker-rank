#include <iostream>
#include <set>

int main( int argc, char* argv[] ) {
    int T, a, b;
    std::set<int> myset;
    std::set<int>::iterator iter;

    std::cin >> T;
    for( int i = 0; i < T; ++i ) {
        std::cin >> a >> b;
        switch( a ) {
            case 1:
                myset.insert( b );
                break;

            case 2:
                iter = myset.find( b );
                if( iter != myset.end() ) {
                    myset.erase( iter );
                }
                break;

            case 3:
                std::cout << ((myset.find(b) != myset.end())? "Yes":"No") << std::endl;
                break;
        }
    }
    return 0;
}

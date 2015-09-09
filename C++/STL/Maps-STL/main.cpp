#include <iostream>
#include <map>

int main( int argc, char* argv[] ) {
    // Number of Queries.
    int Q;

    // The type of query and the value to be placed into the map.
    int type, y;

    // They key of the map where the value should be placed into.
    std::string x;

    // The map that holds the data.
    std::map<std::string, int> mymap;

    std:: cin >> Q;
    for( int i = 0; i < Q; ++i ) {
        std::cin >> type;
        switch( type ) {
            // Insert or update a value.
            case 1:
                std::cin >> x >> y;
                if( mymap.find(x) == mymap.end() ) {
                    mymap[x] = 0;
                }

                mymap[x] += y;
                break;

            // Remove from the map.
            case 2:
                std::cin >> x;
                mymap.erase(x);
                break;

            // Print a value from the map.
            case 3:
                std::cin >> x;
                if( mymap.find(x) != mymap.end() ) {
                    std::cout << mymap[x] << std::endl;
                }
                else {
                    std::cout << 0 << std::endl;
                }
                break;
        }
    }
    return 0;
}

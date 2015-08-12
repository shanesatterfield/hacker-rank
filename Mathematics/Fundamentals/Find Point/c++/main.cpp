#include <iostream>
#include <vector>

std::vector<int> find_point( int px, int py, int qx, int qy );

int main( int argc, char* argv[] ) {
    int T, px, py, qx, qy;
    std::cin >> T;

    for( int i = 0; i < T; ++i ) {
        std::cin >> px >> py >> qx >> qy;
        std::vector<int> ans = find_point( px, py, qx, qy );
        std::cout << ans[0] << " " << ans[1] << std::endl;
    }

    return 0;
}

std::vector<int> find_point( int px, int py, int qx, int qy ) {
    std::vector<int> ans;
    ans.push_back( 2*qx - px );
    ans.push_back( 2*qy - py );
    return ans;
}

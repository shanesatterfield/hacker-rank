#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

struct Point {
    int num;
    int min;
};

int minimax( int p, int q, std::vector<int> vec )
{
    std::sort(vec.begin(), vec.end());
    int curr, temp;

    Point highest = {p, 0};
    int starting  = 0;
    int n         = p;
    int max_range = q;

    if( q > vec.back() )
    {
        highest.num = q;
        highest.min = abs(vec.back() - q);
    }

    while( n <= max_range && starting < vec.size() )
    {
        curr = std::numeric_limits<int>::max();

        for( int i = starting; i < vec.size(); ++i )
        {
            temp = abs(vec[i] - n);
            if( temp <= highest.min )
            {
                curr     = temp;
                starting = i;
                break;
            }

            else if( temp >= curr )
                break;

            else
            {
                curr     = temp;
                starting = i;
            }
        }

        if( curr > highest.min && curr < std::numeric_limits<int>::max() )
        {
            highest.num = n;
            highest.min = curr;
        }

        n = std::max(n+1, vec[starting] + highest.min + 1);
    }

    return highest.num;
}

int main( int argc, char* argv[] )
{
    int n, p, q, temp;
    std::vector<int> vec;

    std::cin >> n;
    for( int i = 0; i < n; ++i )
    {
        std::cin >> temp;
        vec.push_back( temp );
    }

    std::cin >> p >> q;
    std::cout << minimax( p, q, vec ) << std::endl;
    return 0;
}

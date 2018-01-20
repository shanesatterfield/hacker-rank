#include <iostream>
#include <math.h>

int fib(int A, int B, int N);

int main(int arg, char* argv[])
{
    int T, A, B, N;
    std::cin >> T;

    for( int i = 0; i < T; ++i )
    {
        std::cin >> A >> B >> N;
        std::cout << fib(A, B, N) << std::endl;
    }

    return 0;
}

int fib(int A, int B, int N)
{
    if(N <= 0)
        return A;
    if(N == 1)
        return B;

    int prev = A;
    int result = B;
    int temp;
    int max_mod = pow(10, 9) + 7;

    for(int i = 2; i <= N; ++i)
    {
        temp = result;
        result += prev;
        prev = temp;

        result %= max_mod;
    }

    return result;
}

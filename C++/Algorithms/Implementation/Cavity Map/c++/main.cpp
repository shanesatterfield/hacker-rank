#include <iostream>
#include <vector>

bool isCavity( int row, int column, std::vector<std::string> &grid );
bool isWall( int row, int column, int N );
bool isLargest( int row, int column, std::vector<std::string> &grid );

int main( int argc, char* argv[] )
{
    int N;
    std::cin >> N;
    std::string line;
    std::vector<std::string> lines;
    for( int i = 0; i < N; ++i )
    {
        std::cin >> line;
        lines.push_back(line);
    }

    for( int row = 0; row < lines.size(); ++row )
    {
        for( int column = 0; column < lines[row].size(); ++column )
        {
            if( isCavity( row, column, lines ) )
            {
                std::cout << 'X';
            }
            else
            {
                std::cout << lines[row][column];
            }
        }
        std::cout << std::endl;
    }

    return 0;
}

bool isCavity( int row, int column, std::vector<std::string> &grid )
{
    return isWall(row, column, grid.size()) == false && isLargest(row, column, grid);
}

bool isWall( int row, int column, int N )
{
    return row == 0 || row == N-1 || column == 0 || column == N-1;
}

bool isLargest( int row, int column, std::vector<std::string> &grid )
{
    char num = grid[row][column];
    return num > grid[row-1][column] && num > grid[row+1][column] && num > grid[row][column-1] && num > grid[row][column+1];
}

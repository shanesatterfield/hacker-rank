#include <iostream>
#include <stdio.h>

struct Student {
    int age;
    std::string firstName;
    std::string lastName;
    int standard;
};

int main( int argc, char* argv[] ) {
    Student st;
    std::cin >> st.age >> st.firstName >> st.lastName >> st.standard;
    std::cout << st.age << " " << st.firstName << " " << st.lastName << " " << st.standard;
    return 0;
}

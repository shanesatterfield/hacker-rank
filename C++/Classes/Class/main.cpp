#include <iostream>
#include <sstream>

class Student;

int main( int argc, char* argv[] ) {
    Student st;
    int age, standard;
    std::string lastName, firstName;

    std::cin >> age >> firstName >> lastName >> standard;
    st.setAge( age );
    st.setFirstName( firstName );
    st.setLastName( lastName );
    st.setStandard( standard );

    std::cout << st.getAge() << '\n' << st.getLastName() << ", " << st.getFirstName() << '\n' << st.getStandard() << '\n' << std::endl;
    std::cout << st.toString();
    return 0;
}

class Student {
public:
    void setAge( int age ) {
        this->age = age;
    }

    int getAge() {
        return this->age;
    }

    void setFirstName( std::string firstName ) {
        this->firstName = firstName;
    }

    std::string getFirstName() {
        return this->firstName;
    }

    void setLastName( std::string lastName ) {
        this->lastName = lastName;
    }

    std::string getLastName() {
        return this->lastName;
    }

    void setStandard( int standard ) {
        this->standard = standard;
    }

    int getStandard() {
        return this->standard;
    }

    std::string toString() {
        std::stringstream ss;
        ss << this->getAge() << ',' << this->getFirstName() << ',' << this->getLastName() << ',' << this->getStandard();
        return ss.str();
    }

private:
    int age;
    std::string firstName;
    std::string lastName;
    int standard;
};

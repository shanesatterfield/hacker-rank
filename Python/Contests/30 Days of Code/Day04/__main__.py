from __future__ import print_function

class Person:
    def __init__(self, initial_age):
        self.setAge(initial_age)

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 18:
            print('You are old.')
        else:
            print('You are a teenager.')

    def yearPasses(self):
        self.age += 1

    def setAge(self, newAge):
        self.age = max(newAge, 0)
        if newAge < 0:
            print('This person is not valid, setting age to 0.')

    def getAge(self):
        return self.age

if __name__ == '__main__':
    # Mandatory code from HackerRank.
    T=int(raw_input())
    for i in range(0,T):
        age=int(raw_input())
        p=Person(age)
        p.amIOld()
        for j in range(0,3):
            p.yearPasses();
        p.amIOld();
        print("")

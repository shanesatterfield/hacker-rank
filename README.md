# hacker-rank
This is a repository of my solutions to [Hacker Rank](https://www.hackerrank.com/) problems.

## Languages
Currently, I have solutions written in
- Python 2 and 3
- Javascript
- Java
- C++
- SQL

## How to Run the Code

## Python
You can run the python code in either python 2 or 3 for most projects, though python 3 support has priority. You can run a package by invoking python on a directory that contains a \_\_main\_\_.py file. For example,
```
python python_song_of_pi/
```

#### Running Tests
You will need to install the dependencies in the requirements.txt file. This includes pytest and pytest-sugar. With those installed, you can run all tests in all subdirecties with the command
```
py.test
```

## Javascript
The javascript scripts can be run from the main.js file. You will need nodejs to run these files and you can run them with the command
```
node main.js
```

#### Running Tests
You will need to have mochajs installed. With npm installed, you can do this with the following command.
```
npm install -g mocha
```

From there, you can run all tests with the command
```
mocha **/test.js
```

If you are with a directory with a test file, you can simply run the `mocha` command to run tests from just that module.

## Coffeescript

You can run the coffeescript solutions by running the following command from the root directory of the coffeescript solution.
```
coffee src/main.coffee
```

#### Running the Tests

You will need to have coffee-script installed locally and mocha installed. You can them run the tests from the root directory off the coffeescript solution.
```
mocha --compilers coffee:coffee-script/register
```

## C++
You can run the C++ code by using the CMake build system. A CMakeLists.txt file is supplied for each solution and a vew top level CMakeLists.txt files that allow you to build all of the C++ solutions from the C++ subdirectory.

#### Compiling the Solutions
You must have a C++ compiler and CMake set up on your system. Then run the following commands from the C++ subdirectory.
```bash
mkdir build && cd build && cmake .. && make
```
You might need to use a different toolchain depending on which compiler you are using and which operating system you are on.

## Java
You will need a Java compiler and Gradle installed on your system. You can navigate to a directory containing a build.gradle file and run the code with the `gradle run` command. Note that you can use quiet mode with gradle to remove the gradle stdout output. To do this add the `-q` flag. Ex: `gradle -q run`.

#### Running the Tests
Some of the Java solutions have tests written for them. You can run these tests with either the commands `gradle test` or `gradle build`. If the tests fail, you will see output telling you which tests failed. If no tests failed, there will be no output.


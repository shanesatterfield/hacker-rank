# hacker-rank
This is a repository of my solutions to hacker rank problems.

## Languages
Currently, I have solutions written in
- Python 2 and 3
- Javascript

## How to Run the Code

## Python
You can run the python code in either python 2 or 3 for most projects, though python 3 support has priority. You can run a package by invoking python on a directory that contains a \_\_main\_\_.py file. For example,
```
python python_song_of_pi/
```

### Running Tests
You will need to install the dependencies in the requirements.txt file. This includes pytest and pytest-sugar. With those installed, you can run all tests in all subdirecties with the command
```
py.test
```

## Javascript
The javascript scripts can be run from the main.js file. You will need nodejs to run these files and you can run them with the command
```
node main.js
```

### Running Tests
You will need to have mochajs installed. With npm installed, you can do this with the following command.
```
npm install -g mocha
```

From there, you can run all tests with the command
```
mocha **/test.js
```

If you are with a directory with a test file, you can simply run the `mocha` command to run tests from just that module.


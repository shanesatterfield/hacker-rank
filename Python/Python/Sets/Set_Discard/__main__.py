from __future__ import print_function
import sys

funcs = {
    'pop':     set.pop,
    'remove':  set.remove,
    'discard': set.discard
}

def setdis(starting_list, commands):
    result = set(starting_list)
    commands_parsed = [cmd.split() for cmd in commands]

    for cmd in commands_parsed:
        if len(cmd) == 2:
            cmd[1] = int(cmd[1])
        funcs[cmd[0]](result, *cmd[1:])
    return sum(result)

def main():
    lines = [ x.strip() for x in sys.stdin.readlines() ]
    starting_list = [ int(x) for x in lines[1].split() ]
    commands = lines[3:]

    print(setdis(starting_list, commands))

if __name__ == '__main__':
    main()

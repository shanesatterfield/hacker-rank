from __future__ import print_function
import sys

class MyList:
    def __init__( self ):
        self.lst = list()

        # A dictitnary of the different commands mapped to their functions.
        self.commands = {
            'print':   lambda *args: print( self.lst ),
            'insert':  lambda *args: self.lst.insert( int(args[0]), int(args[1]) ),
            'remove':  lambda *args: self.lst.remove( int(args[0]) ),
            'append':  lambda *args: self.lst.append( int(args[0]) ),
            'sort':    lambda *args: self.lst.sort(),
            'pop':     lambda *args: self.lst.pop(),
            'reverse': lambda *args: self.lst.reverse(),
        }

    def run_cmd( self, command ):
        """If the command is in the map, it will run it on the list."""
        command = command.split()
        if command[0] in self.commands:
            self.commands[ command[0] ]( *command[1:] )

def main():
    T     = int(input())
    lines = sys.stdin.readlines()[:T]
    lst   = MyList()

    for line in lines:
        lst.run_cmd( line )

if __name__ == '__main__':
    main()

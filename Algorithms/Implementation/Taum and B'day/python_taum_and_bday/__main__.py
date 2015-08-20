from __future__ import print_function, division
import sys

def taum( b, w, x, y, z ):
    lst = sorted([(b, x), (w, y), (b, y+z), (w, x+z)], key=lambda x: x[1])
    return sum([ x[0] * x[1] for x in lst[:2] ])


def main():
    lines = [ x.strip() for x in sys.stdin.readlines() ]
    T = int(lines[0].strip())
    lines = lines[1:]
    for n in range(T):
        b, w    = [ int(x) for x in lines[n*2].split() ]
        x, y, z = [ int(x) for x in lines[n*2+1].split() ]
        print(taum(b,w,x,y,z))

if __name__ == '__main__':
    main()

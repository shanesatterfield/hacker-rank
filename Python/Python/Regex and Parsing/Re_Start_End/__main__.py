from __future__ import print_function
import sys, re

def restart(text, sub):
    pat = re.compile(sub)
    temp = pat.search(text)
    if temp == None:
        return [(-1, -1)]

    results = [(temp.start(), temp.end()-1)]
    # Search again, but start from just after the starting point of
    # the previous find.
    while True:
        offset = results[-1][0]+1
        temp = pat.search(text[offset:])
        if temp == None or offset >= len(text):
            break

        results.append((temp.start()+offset, temp.end()+offset-1))
    return results

def main():
    lines = sys.stdin.readlines()[:2]
    for line in restart(*lines):
        print(line)

if __name__ == '__main__':
    main()

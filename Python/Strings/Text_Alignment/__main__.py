from __future__ import print_function, division

char = 'H'
space = ' '

def text_align(width):
    lines = []
    for n in range(width):
        lines.append((char*(n*2+1)).center(width*2-1, space))

    offset = space*(width*4 - (width*2-1))

    for n in range(width+1):
        lines.append((char*width).center(width*2-1, space) + offset + (char*width).center(width*2-1, space))

    for n in range((width+1)//2):
        lines.append((char*width*5).center(width*6, space))

    for n in range(width+1):
        lines.append((char*width).center(width*2-1, space) + offset + (char*width).center(width*2-1, space))

    for n in reversed(range(width)):
        lines.append(space*(width*4) + (char*(n*2+1)).center(width*2-1, space))

    return lines

def main():
    T = int(input())
    print('\n'.join(text_align(T)))

if __name__ == '__main__':
    main()

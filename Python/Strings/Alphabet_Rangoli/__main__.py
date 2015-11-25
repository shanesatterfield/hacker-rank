from __future__ import print_function

def rangoli(iterations, space='-'):
    result = []
    starting = ord('a') + iterations - 1
    width = (iterations - 1) * 4 + 1

    if iterations == 1:
        return ['a']
    elif iterations <= 0:
        return []

    for i in range(iterations):
        row = []
        curr = 0
        while curr <= i:
            row.append(chr(starting - curr))
            row.append(space)
            curr += 1
        row.extend(list(reversed(row[:-3])))
        result.append(''.join(row).center(width, space))

    result.extend(list(reversed(result[:-1])))
    return result

def main():
    for line in rangoli(int(input())):
        print(line)

if __name__ == '__main__':
    main()

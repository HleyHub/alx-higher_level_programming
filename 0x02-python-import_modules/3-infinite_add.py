#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    arguments = 0
    for j in range(1, len(argv)):
        arguments = arguments + int(argv[j])
    print(arguments)

#!/usr/bin/python3
"""
    Script that reads stdin line by line and computes metrics
"""
import sys


def print_metrics(sc, fs):
    """
    A function that prints the total file size and the
    number of occurrences for each status code.
    Args:
        sc (dict): A dictionary containing status codes.
        fs (int): The total file size.
    Returns:
        None
    """
    print(f"File size: {fs}")
    for code in sorted(sc.keys()):
        print(f"{code}: {sc[code]}")


def parse_log_line(line, sc, fs):
    """
    Parses a log line, updates status codes and total file size accordingly
    Args:
        line (str): The log line to be parsed.
        sc (dict): A dictionary containing status codes.
        fs (int): The total file size.
    Returns:
        tuple: A tuple containing updated status codes and total file size
    """

    elts = line.strip().split(" ")
    if len(elts) == 9:
        code = elts[7]
        file_size = int(elts[8])
        fs += file_size
        if code in sc:
            sc[code] += 1
        else:
            sc[code] = 1
    return sc, fs


def main():
    """
    A main function to read log lines, parse them, and print metrics
    """

    sc = {}
    fs = 0
    lc = 0

    try:
        for line in sys.stdin:
            sc, fs = parse_log_line(line, sc, fs)
            lc += 1

            if lc % 10 == 0:
                print_metrics(sc, fs)

    except KeyboardInterrupt:
        pass

    print_metrics(sc, fs)


if __name__ == "__main__":
    main()

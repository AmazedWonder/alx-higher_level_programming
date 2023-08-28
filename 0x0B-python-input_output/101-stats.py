#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.

This is a script that reads input from sys.stdin, accumulates metrics
such as file size and status code counts, and periodically prints the
accumulated metrics. It also catches the KeyboardInterrupt exception
to print the metrics and re-raises the exception.

How the code works:

The print_stats function takes two arguments: size (the accumulated
file size) and status_codes (a dictionary representing the accumulated
count of status codes). It prints the file size and then iterates over
the keys of status_codes in sorted order, printing each key-value pair.

The script initializes variables size (initialized to 0), status_codes
(initialized as an empty dictionary), valid_codes (a list of valid
status codes), and count (initialized to 0).

The script then enters a loop that reads lines from sys.stdin. It
processes each line while keeping track of the count of lines read
(count). When count reaches 10, it calls print_stats with the
accumulated size and status_codes, and resets count to 1.
Otherwise, it increments count by 1.

For each line, it splits the line into a list of words. It tries
to extract the file size from the last element of the line
(line[-1]) and adds it to size if it can be converted to an integer.

It also tries to extract the status code from the second-to-last
element of the line (line[-2]). If the status code is valid
(found in valid_codes), it updates the count in the status_codes
dictionary accordingly. If the status code is not found in status_codes,
it adds it as a new key with a count of 1. Otherwise, it increments
the existing count by 1.

After processing all input lines, it calls print_stats one final
time to print the accumulated metrics.

The script catches the KeyboardInterrupt exception, which occurs
when the user interrupts the program (e.g., by pressing Ctrl+C).
In such cases, it calls print_stats to print the accumulated metrics
and then re-raises the exception, allowing the program to terminate.

Overall, the script reads input lines, accumulates file size and
status code counts, periodically prints the accumulated metrics,
and handles user interrupts gracefully by printing the metrics
before terminating.

"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

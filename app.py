# -*- coding: utf-8 -*-
"""A simple python program."""

import argparse

from dateutil.parser import parse

def main():
    """Parse the passed date and print it."""
    # Parse some arguments.
    parser = argparse.ArgumentParser(description='A simple argparse.')
    parser.add_argument('-t', '--time',  required=True,
        help='The time to parse.')
    args = vars(parser.parse_args())

    # Turn the parsed time into a datetime with timezone info.
    time = parse(args['time'])

    # Print the time.
    print(time)


if __name__ == '__main__':
    main()

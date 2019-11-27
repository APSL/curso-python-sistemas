#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
    parser.add_argument("-n", "--num", help="float number",
                    type=float, default=0.1)

    args = parser.parse_args()
    if args.verbose:
        print("verbosity turned on")

    print("num: {}".format(args.num))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
    Blazed City
    Demo implementation of the Blazed City standard in
    Python. In this demo, three towns are provisioned
    with some default starter data (and keys). For
    security purposes, only the public keys are published.
    If you would like to compile and run this, you will have to
    regenerate they public and private keys, or use some other keys
    you have lying around. RSA 2048 (public [.pub], private, .ppk)
    (c)2022 ALL RIGHTS RESERVED. MIT LICENSED.
    BLAZED LABS LLC.; BLAZED SYSTEMS BD. BLAZED PUBLISHING BD.
"""

__author__ = "Blazed Labs LLC"
__version__ = "0.3.0"
__license__ = "MIT"

import argparse


def main(args):
    """ Main entry point of the software """
    print("Welcome to the World...")
    print(args)

    # The entire implimentation of a City depends upon a context
    town_list = ["swell", "magnolia", "ferringwood"]
    i = 1
    towns = []
    for town_name in town_list:
        town.append(i, town(town_name))
        i += 1
    city = context("blazed")
    city.set_towns(towns)
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
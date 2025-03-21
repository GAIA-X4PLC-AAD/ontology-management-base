#!/usr/bin/env python3
import os
import sys

from rdflib import Graph
from rdflib.exceptions import ParserError


def lint_file(filename):
    try:
        g = Graph()
        g.parse(filename, format="turtle")
        return 0
    except ParserError as e:
        sys.stderr.write(f"❌ {filename} is not valid Turtle:\n{e}\n")
        return 1


def main():
    ret = 0
    for filename in sys.argv[1:]:
        ret |= lint_file(os.path.normpath(filename))
    sys.exit(ret)


if __name__ == "__main__":
    main()

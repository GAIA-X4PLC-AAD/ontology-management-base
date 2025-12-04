#!/usr/bin/env python3
import argparse
import io
import os
import sys

from rdflib import Graph
from rdflib.exceptions import ParserError


def check_parse_turtle(filename):
    if not os.path.isfile(filename):
        sys.stderr.write(f"❌ File not found: {filename}\n")
        return 1

    try:
        g = Graph()
        g.parse(filename, format="turtle")
        print(f"✅ Successfully parsed: {filename}\n")
        return 0
    except ParserError as e:
        sys.stderr.write(f"❌ {filename} is not valid Turtle:\n{e}\n")
        return 1
    except Exception as e:
        sys.stderr.write(f"❌ Unexpected error parsing {filename}:\n{e}\n")
        return 1


def gather_turtle_files(paths):
    files = []
    for path in paths:
        if os.path.isdir(path):
            for root, _, filenames in os.walk(path):
                for name in filenames:
                    if name.endswith(".ttl"):
                        files.append(os.path.join(root, name))
        elif os.path.isfile(path) and path.endswith(".ttl"):
            files.append(path)
        else:
            sys.stderr.write(f"⚠️ Ignoring invalid path or unsupported file: {path}\n")
    return files


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Validate Turtle files by parsing them."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to validate")
    args = parser.parse_args(args)

    files = gather_turtle_files(args.paths)
    if not files:
        sys.stderr.write("❌ No valid Turtle files found.\n")
        sys.exit(1)

    ret = 0
    for filename in files:
        ret |= check_parse_turtle(os.path.normpath(filename))
    sys.exit(ret)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()

#!/usr/bin/env python3
import json
import sys


def lint_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        return 0
    except json.JSONDecodeError as e:
        sys.stderr.write(f"❌ {filename} is not valid JSON:\n{e}\n")
        return 1


def main():
    ret = 0
    for filename in sys.argv[1:]:
        ret |= lint_file(filename)
    sys.exit(ret)


if __name__ == "__main__":
    main()

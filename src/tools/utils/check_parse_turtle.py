#!/usr/bin/env python3
import argparse
import io
import os
import sys

from rdflib import Graph
from rdflib.exceptions import ParserError


def check_parse_turtle(filename):
    """
    Check a single Turtle (.ttl) file.

    Returns
    -------
    (return_code, message) : (int, str)
        return_code == 0 if OK, 1 otherwise
        message is a human-readable status/error message.
    """
    if not os.path.isfile(filename):
        msg = f"❌ File not found: {filename}"
        return 1, msg

    try:
        g = Graph()
        g.parse(filename, format="turtle")
        msg = f"✅ Successfully parsed: {filename}"
        return 0, msg
    except ParserError as e:
        msg = f"❌ {filename} is not valid Turtle:\n{e}"
        return 1, msg
    except Exception as e:
        msg = f"❌ Unexpected error parsing {filename}:\n{e}"
        return 1, msg


def gather_turtle_files(paths):
    """
    Gather all .ttl files from the given paths.

    For CLI use. Other scripts can call this as well if needed.
    """
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
            # Still write directly to stderr for invalid/unsupported paths
            sys.stderr.write(f"⚠️ Ignoring invalid path or unsupported file: {path}\n")
    return files


def validate_turtle_files(paths):
    """
    Validate all Turtle files found in the given paths.

    Parameters
    ----------
    paths : list[str]
        List of files or directories.

    Returns
    -------
    (return_code, results) : (int, list[tuple[int, str]])
        return_code is the aggregated return code (0 if all OK).
        results is a list of (code, message) for each checked file
        and global errors like “no files”.
    """
    results = []
    files = gather_turtle_files(paths)

    if not files:
        msg = "❌ No valid Turtle files found."
        results.append((1, msg))
        return 1, results

    ret = 0
    for filename in files:
        filename = os.path.normpath(filename)
        code, msg = check_parse_turtle(filename)
        results.append((code, msg))
        ret |= code

    return ret, results


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Validate Turtle files by parsing them."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to validate")
    parsed_args = parser.parse_args(args)

    ret, results = validate_turtle_files(parsed_args.paths)

    # Print messages based on return code
    for code, msg in results:
        if code == 0:
            sys.stdout.write(msg + "\n")
        else:
            sys.stderr.write(msg + "\n")

    sys.exit(ret)


if __name__ == "__main__":
    # Ensure UTF-8 output for emojis, etc.
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()

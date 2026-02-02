#!/usr/bin/env python3
import argparse
import io
import os
import sys
from pathlib import Path

from rdflib import Graph
from rdflib.exceptions import ParserError

from src.tools.utils.file_collector import collect_turtle_files
from src.tools.utils.print_formatter import normalize_path_for_display


def check_turtle_wellformedness(filename, root_dir: Path = None):
    """
    Check if a single file contains syntactically correct (well-formed) Turtle.

    This does NOT validate logical consistency or SHACL compliance.
    It merely ensures the file can be parsed by an RDF parser.

    Returns
    -------
    (return_code, message) : (int, str)
        return_code == 0 if OK, 1 otherwise
        message is a human-readable status/error message.
    """
    # Normalize path for display
    if root_dir:
        display_path = normalize_path_for_display(filename, root_dir)
    else:
        display_path = str(filename)

    if not os.path.isfile(filename):
        msg = f"❌ File not found: {display_path}"
        return 1, msg

    try:
        g = Graph()
        # strictly parse as turtle
        g.parse(filename, format="turtle")
        msg = f"✅ Syntax OK: {display_path}"
        return 0, msg
    except ParserError as e:
        msg = f"❌ Syntax Error in {display_path}:\n{e}"
        return 1, msg
    except Exception as e:
        msg = f"❌ Unexpected error parsing {display_path}:\n{e}"
        return 1, msg


def gather_turtle_files(paths):
    """
    Gather all .ttl files from the given paths.

    For CLI use. Other scripts can call this as well if needed.

    Note: This function now delegates to the central file_collector utility.
    """
    return collect_turtle_files(paths, warn_on_invalid=True, return_pathlib=False)


def verify_turtle_syntax(paths, root_dir: Path = None):
    """
    Verify syntax correctness for all Turtle files found in the given paths.

    Parameters
    ----------
    paths : list[str]
        List of files or directories.
    root_dir : Path, optional
        Root directory for normalizing paths in output

    Returns
    -------
    (return_code, results) : (int, list[tuple[int, str]])
        return_code is the aggregated return code (0 if all OK).
        results is a list of (code, message) for each checked file
        and global errors like "no files".
    """
    results = []
    files = gather_turtle_files(paths)

    if not files:
        msg = "⚠️ No Turtle files found to check."
        results.append((1, msg))
        return 1, results

    ret = 0
    for filename in files:
        filename = os.path.normpath(filename)
        # Call the renamed function that checks for well-formedness
        code, msg = check_turtle_wellformedness(filename, root_dir)
        results.append((code, msg))
        ret |= code

    return ret, results


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Verify syntax correctness (well-formedness) of Turtle files."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to check")
    parsed_args = parser.parse_args(args)

    ret, results = verify_turtle_syntax(parsed_args.paths)

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

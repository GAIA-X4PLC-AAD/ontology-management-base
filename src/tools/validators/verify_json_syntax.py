#!/usr/bin/env python3
import argparse
import io
import json
import os
import sys
from pathlib import Path

from src.tools.utils import collect_jsonld_files, normalize_path_for_display


def check_json_wellformedness(filename, root_dir: Path = None):
    """
    Check if a single file contains syntactically correct (well-formed) JSON.

    This does NOT validate the JSON-LD structure or SHACL compliance.
    It merely ensures the file can be parsed by the JSON loader.

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
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        msg = f"✅ Syntax OK: {display_path}"
        return 0, msg
    except json.JSONDecodeError as e:
        msg = f"❌ Syntax Error in {display_path}:\n   Line {e.lineno}, Col {e.colno}: {e.msg}"
        return 1, msg
    except Exception as e:
        msg = f"❌ Unexpected error parsing {display_path}:\n{e}"
        return 1, msg


def gather_jsonld_files(paths):
    """
    Gather all .json / .jsonld files from the given paths.

    For use from main(). Other scripts can call this as well if they like.

    Note: This function now delegates to the central file_collector utility.
    """
    return collect_jsonld_files(paths, warn_on_invalid=True, return_pathlib=False)


def verify_json_syntax(paths, root_dir: Path = None):
    """
    Verify syntax correctness for all JSON/JSON-LD files found in the given paths.

    Parameters
    ----------
    paths : list[str]
        List of files or directories.
    root_dir : Path, optional
        Root directory for normalizing paths in output

    Returns
    -------
    (return_code, messages) : (int, list[str])
        return_code is the aggregated return code (0 if all OK).
        messages is a list of status/error strings for each file and errors.
    """
    results = []
    files = gather_jsonld_files(paths)

    if not files:
        msg = "⚠️ No JSON-LD files found to check."
        results.append((1, msg))
        return 1, results

    ret = 0
    for filename in files:
        filename = os.path.normpath(filename)
        # Call the renamed function that checks for well-formedness
        code, msg = check_json_wellformedness(filename, root_dir)
        results.append((code, msg))
        ret |= code

    return ret, results


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Verify syntax correctness (well-formedness) of JSON-LD files."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to check")
    parsed_args = parser.parse_args(args)

    ret, results = verify_json_syntax(parsed_args.paths)

    # results is now a list of tuples: (code, message)
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

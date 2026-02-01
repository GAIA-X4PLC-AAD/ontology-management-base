#!/usr/bin/env python3
import argparse
import io
import json
import os
import sys


def check_parse_jsonld(filename):
    """
    Check a single JSON/JSON-LD file.

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
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        msg = f"✅ Successfully parsed: {filename}"
        return 0, msg
    except json.JSONDecodeError as e:
        msg = f"❌ {filename} is not valid JSON:\n{e}"
        return 1, msg
    except Exception as e:
        msg = f"❌ Unexpected error parsing {filename}:\n{e}"
        return 1, msg


def gather_jsonld_files(paths):
    """
    Gather all .json / .jsonld files from the given paths.

    For use from main(). Other scripts can call this as well if they like.
    """
    files = []
    for path in paths:
        if os.path.isdir(path):
            for root, _, filenames in os.walk(path):
                for name in filenames:
                    if name.endswith((".json", ".jsonld")):
                        files.append(os.path.join(root, name))
        elif os.path.isfile(path) and path.endswith((".json", ".jsonld")):
            files.append(path)
        else:
            # This is still written directly to stderr because it's about CLI usage
            sys.stderr.write(f"⚠️ Ignoring invalid path or unsupported file: {path}\n")
    return files


def validate_jsonld_files(paths):
    """
    Validate all JSON/JSON-LD files found in the given paths.

    Parameters
    ----------
    paths : list[str]
        List of files or directories.

    Returns
    -------
    (return_code, messages) : (int, list[str])
        return_code is the aggregated return code (0 if all OK).
        messages is a list of status/error strings for each file and errors.
    """
    results = []
    files = gather_jsonld_files(paths)

    if not files:
        msg = "❌ No valid JSON-LD files found."
        results.append((1, msg))
        return 1, results

    ret = 0
    for filename in files:
        filename = os.path.normpath(filename)
        code, msg = check_parse_jsonld(filename)
        results.append((code, msg))
        ret |= code

    return ret, results


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Validate JSON-LD files by parsing them."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to validate")
    parsed_args = parser.parse_args(args)

    ret, results = validate_jsonld_files(parsed_args.paths)

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

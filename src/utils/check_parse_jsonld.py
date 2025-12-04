#!/usr/bin/env python3
import argparse
import io
import json
import os
import sys


def check_parse_jsonld(filename):
    if not os.path.isfile(filename):
        sys.stout.write(f"❌ File not found: {filename}\n")
        return 1

    try:
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        print(f"✅ Successfully parsed: {filename}\n")
        return 0
    except json.JSONDecodeError as e:
        sys.stderr.write(f"❌ {filename} is not valid JSON:\n{e}\n")
        return 1
    except Exception as e:
        sys.stderr.write(f"❌ Unexpected error parsing {filename}:\n{e}\n")
        return 1


def gather_jsonld_files(paths):
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
            sys.stderr.write(f"⚠️ Ignoring invalid path or unsupported file: {path}\n")
    return files


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Validate JSON-LD files by parsing them."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to validate")
    args = parser.parse_args(args)

    files = gather_jsonld_files(args.paths)
    if not files:
        sys.stderr.write("❌ No valid JSON-LD files found.\n")
        sys.exit(1)

    ret = 0
    for filename in files:
        ret |= check_parse_jsonld(os.path.normpath(filename))
    sys.exit(ret)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()

import io
import os
import sys
import textwrap

from rdflib import Graph, exceptions
from rdflib.plugins.parsers.notation3 import BadSyntax


def check_ttl_syntax(turtle_file: str) -> tuple[int, str]:
    """
    Check the Turtle syntax of the given file.

    Returns:
        (return_code, message)
        return_code: 0 if syntax is correct, 200 on syntax error, other codes can be used for other errors.
        message: descriptive success or error message.
    """
    g = Graph()
    try:
        with open(turtle_file, "r", encoding="utf-8") as f:
            content = f.read()
        g.parse(data=content, format="turtle")
        return 0, f"The file {turtle_file} is syntactically correct."
    except (exceptions.Error, BadSyntax) as e:
        width = 150
        border_line = "=" * width

        # Create a centered header for the error
        header_text = f"Syntax error in file: {turtle_file}"
        header_line = "=" + header_text.center(width - 2) + "="

        # Wrap the error details so that each line fits in the available width
        error_details = f"Error details: {e}"
        wrapped_lines = []
        for line in error_details.splitlines():
            wrapped_lines.extend(textwrap.wrap(line, width=width - 2) or [""])
        error_lines = "\n".join(
            "= " + line.ljust(width - 3) + "=" for line in wrapped_lines
        )

        # Combine the parts into one output block
        output = f"{border_line}\n{header_line}\n{error_lines}\n{border_line}\n"
        return 200, output


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_ttl_syntax.py <ttl_file>", file=sys.stderr)
        sys.exit(100)

    ttl_file = os.path.normpath(sys.argv[1])
    if not ttl_file.endswith(".ttl"):
        print(f"Error: {ttl_file} is not a Turtle (.ttl) file.", file=sys.stderr)
        sys.exit(110)

    return_code, message = check_ttl_syntax(ttl_file)
    if return_code != 0:
        print(message, file=sys.stderr)
        sys.exit(return_code)
    else:
        print(message)
        sys.exit(0)


if __name__ == "__main__":
    # Set the encoding for stdout and stderr to UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    main()

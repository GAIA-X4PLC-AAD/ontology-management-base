import sys
from rdflib import Graph, exceptions


def check_ttl_syntax(turtle_file: str):
    g = Graph()
    try:
        g.parse(turtle_file, format='turtle')
        print(f"The file {turtle_file} is syntactically correct.")
    except exceptions.Error as e:
        print(f"Syntax error in the file {turtle_file}: {e}")
        sys.exit(2)


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_ttl_syntax.py <ttl_file>")
        sys.exit(1)

    ttl_file = sys.argv[1]
    check_ttl_syntax(ttl_file)


if __name__ == "__main__":
    main()

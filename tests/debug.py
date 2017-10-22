
import argparse
from py2nb.tools import python_to_notebook

description = """
Convert literate python script into Jupyter Notebook
"""


def main():
    ap = argparse.ArgumentParser(description=description)
    ap.add_argument("--source", help="python filename",
                    default='tests/hello.py')
    ap.add_argument("--destination", help="output notebook filename",
                    default='tests/debug.ipynb')
    args = ap.parse_args()
    # Process
    python_to_notebook(input_filename=args.source,
                       output_filename=args.destination)

if __name__ == '__main__':
    main()

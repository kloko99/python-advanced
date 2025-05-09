"""
python -m supertool
"""

import sys


def main():
    print(sys.path)  # hier guckt Python nach den Imports
    print("__main__")


if __name__ == "__main__":
    main()

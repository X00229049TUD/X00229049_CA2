from __future__ import annotations

import argparse

from calculator import add, subtract


def build_parser() -> argparse.ArgumentParser:
    """
    Create and return the argument parser.
    """
    parser = argparse.ArgumentParser(description="Simple Calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_cmd = subparsers.add_parser("add", help="Add two numbers")
    add_cmd.add_argument("a", type=float, help="First number")
    add_cmd.add_argument("b", type=float, help="Second number")

    sub_cmd = subparsers.add_parser("sub", help="Subtract two numbers")
    sub_cmd.add_argument("a", type=float, help="First number")
    sub_cmd.add_argument("b", type=float, help="Second number")

    return parser


def main() -> None:
    """
    Parse arguments and perform the requested operation.
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        result = add(args.a, args.b)
    elif args.command == "sub":
        result = subtract(args.a, args.b)
    else:
        parser.error("Unknown command")
        return

    print(result)


if __name__ == "__main__":
    main()
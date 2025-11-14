"""
main module
"""

from __future__ import annotations

import argparse
from typing import Callable, Dict

from calculator import add, subtract, multiply, divide


OperationFunc = Callable[[float, float], float]


def build_parser() -> argparse.ArgumentParser:
    """
    Create and return the argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Simple calculator with basic arithmetic operations."
    )
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform.",
    )
    parser.add_argument("a", type=float, help="First operand.")
    parser.add_argument("b", type=float, help="Second operand.")
    return parser


def main() -> None:
    """
    Entry point for the CLI.
    """
    parser = build_parser()
    args = parser.parse_args()

    operations: Dict[str, OperationFunc] = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
    }

    func = operations[args.operation]

    try:
        result = func(args.a, args.b)
    except ValueError as exc:
        # For example, division by zero.
        parser.error(str(exc))
        return

    print(result)


if __name__ == "__main__":
    main()

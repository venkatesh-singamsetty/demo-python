"""Simple example application.

Provides a `greet` function and a CLI `main` entrypoint.
"""
from __future__ import annotations

import argparse
from typing import Optional


def greet(name: Optional[str] = None) -> str:
    """Return a greeting for `name` or a default greeting."""
    if not name:
        name = "World"
    return f"Hello, {name}!"


def main(argv: Optional[list[str]] = None) -> int:
    """CLI entrypoint. Returns exit code 0 on success."""
    parser = argparse.ArgumentParser(description="Simple greeting CLI")
    parser.add_argument("--name", "-n", help="Name to greet", default=None)
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

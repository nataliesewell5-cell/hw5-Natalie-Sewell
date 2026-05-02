#!/usr/bin/env python3
"""
weighted-decision-roller: roll_decision.py

Takes a comma-separated string of "option:weight" pairs and picks a
winner using a weighted dice roll. Uses secrets.randbelow() for
cryptographically fair randomness (not AI-guessed randomness).

Usage:
    python roll_decision.py "Alice:3,Bob:1,Carol:5"
"""

import sys
import secrets


def parse_options(raw: str) -> list[tuple[str, int]]:
    options = []
    for part in raw.strip().split(","):
        part = part.strip()
        if ":" not in part:
            raise ValueError(f"Missing weight for option: '{part}'. Use format Name:Weight")
        name, weight_str = part.rsplit(":", 1)
        name = name.strip()
        weight_str = weight_str.strip()
        if not name:
            raise ValueError("Option name cannot be empty.")
        try:
            weight = int(weight_str)
        except ValueError:
            raise ValueError(f"Weight for '{name}' must be a whole number, got: '{weight_str}'")
        if weight < 1:
            raise ValueError(f"Weight for '{name}' must be at least 1, got: {weight}")
        options.append((name, weight))
    return options


def roll(options: list[tuple[str, int]]) -> dict:
    total = sum(w for _, w in options)
    if total < 2:
        raise ValueError("Total ticket pool must be at least 2.")
    if len(options) < 2:
        raise ValueError("Must provide at least 2 options.")
    if len(options) > 50:
        raise ValueError("Maximum 50 options allowed.")

    roll_number = secrets.randbelow(total) + 1

    cursor = 0
    winner = None
    for name, weight in options:
        cursor += weight
        if roll_number <= cursor:
            winner = (name, weight)
            break

    pct = (winner[1] / total) * 100
    return {
        "winner": winner[0],
        "roll": roll_number,
        "total_tickets": total,
        "winner_tickets": winner[1],
        "winner_pct": round(pct, 1),
    }


def main():
    if len(sys.argv) < 2:
        print("ERROR: No options provided.")
        print('Usage: python roll_decision.py "Alice:3,Bob:1,Carol:5"')
        sys.exit(1)

    raw = sys.argv[1]

    try:
        options = parse_options(raw)
        result = roll(options)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print(f"TOTAL_TICKETS={result['total_tickets']}")
    print(f"ROLL={result['roll']}")
    print(f"WINNER={result['winner']}")
    print(f"WINNER_TICKETS={result['winner_tickets']}")
    print(f"WINNER_PCT={result['winner_pct']}")


if __name__ == "__main__":
    main()

# weighted-decision-roller

## What it does
Picks a winner from a list of options using weighted dice rolls.
Each option is assigned a number of "tickets," and the script rolls
across the full ticket pool to select a winner fairly.

## Why I chose it
Weighted random selection is a genuinely useful real-world task —
used in raffles, loot tables, A/B testing, and decision-making.
A language model cannot reliably generate true random numbers,
so the Python script (using `secrets.randbelow`) is load-bearing.

## How to use it
1. Give the agent a list of options with weights, e.g.:
   "Alice:3, Bob:1, Carol:5"
2. The agent reads SKILL.md, runs the script, and reports the winner.

## What the script does
`scripts/roll_decision.py` parses the option:weight pairs, builds a
ticket pool, rolls a cryptographically random number, and walks the
pool to find the winner. It also validates inputs and raises clear
errors for bad data.

## What worked well
- The `secrets` module makes rolls genuinely fair, not pseudo-random
- Error messages are clear and actionable
- The script is easy to extend (e.g. roll history, multiple draws)

## Limitations
- Weights must be whole numbers
- No roll history stored between sessions
- Max 50 options per roll

## Video Demo
[Link goes here]

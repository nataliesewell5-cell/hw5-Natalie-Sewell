---
name: weighted-decision-roller
description: >
  Picks a winner from a list of options using weighted dice rolls — each
  option can be assigned a weight (number of "tickets"), and the script
  rolls a fair die across the total ticket pool to select one. Use when
  the user wants to randomly choose between options that are NOT equally
  likely, such as a raffle, a weighted spin-the-wheel, a loot table, or
  a prioritized decision. Do NOT use for simple equal-probability picks
  (use a plain random choice instead) or when the user wants a
  deterministic/manual decision.
---

## When to use this skill

Use this skill when the user provides a list of options where each option
has a different weight, likelihood, or number of "tickets." Examples:

- "Pick a random pizza topping but pepperoni is twice as likely"
- "Run a raffle: Alice has 3 tickets, Bob has 1, Carol has 5"
- "Weighted loot drop: common=50, rare=30, epic=15, legendary=5"

## When NOT to use this skill

- All options are equally likely → use a simple random picker instead
- The user wants a manual or deliberate choice, not a random one
- Fewer than 2 options are provided

## Expected inputs

The user must provide:
1. A list of options (names, items, people, outcomes)
2. A weight for each option (whole number ≥ 1, representing "tickets")

If weights are missing, ask the user to supply them before proceeding.

## Step-by-step instructions

1. Parse the user's options and weights from their message
2. Confirm the inputs look correct (at least 2 options, all weights ≥ 1)
3. Run the script: `python scripts/roll_decision.py "<option1:weight1,option2:weight2,...>"`
4. Read the script output — it returns the winner, the roll number, and the total ticket pool
5. Present the result clearly to the user, including the odds of the winning option

## Expected output format

Present results like this:

> 🎲 Rolling across **9 total tickets**...
> 🎯 Roll landed on ticket **#7** → **Carol wins!**
> (Carol had 5 tickets = 55.6% chance)

## Limitations

- Weights must be whole numbers (no decimals)
- Maximum 50 options at a time
- Script uses Python's `secrets` module for cryptographically fair randomness
- The skill does not store history between rolls

Scroll down and click the green "Commit changes" button
Click "Commit changes" again on the popup

"""Practicing counters."""

num_string: str = "123"

num_odds: int = 0

if int(num_string[0]) % 2 == 1:
    num_odds = num_odds + 1

if int(num_string[1]) % 2 == 1:
    num_odds = num_odds + 1

if int(num_string[2]) % 2 == 1:
    num_odds = num_odds + 1

print(num_odds)
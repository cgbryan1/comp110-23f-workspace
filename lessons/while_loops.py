"""Demonstrates while loops by finding low value in string."""

cards: str = "5235"
index: int = 0
low: int = int(cards[0])

# look at each number in the string

while index < 4:
    current_card: int = int(cards[index])
    if (current_card < low):
        # update low val to be val of current card
        low = current_card
    index += 1
print(low)
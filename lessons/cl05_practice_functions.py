"""hi."""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("thursday")
print(mimic("hey"))


def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the characters of my_words at index letter_idx."""
    if letter_idx >= len(my_words):
        return "Too high of an index"
    else:
        return my_words[letter_idx]
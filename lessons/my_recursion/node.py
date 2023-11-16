"""Node class for linked list using recursion."""

# Change folder name to not be recursion so I can import recursion.

from __future__ import annotations

class Node:
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Making it print pretty."""
        if self.next is None:
            # base case
            return str(self.data)
        else:
            # recursive step
            return str(self.data) + "->" + str(self.next)
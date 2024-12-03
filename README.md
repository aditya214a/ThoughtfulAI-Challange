# ThoughtfulAI-Challange

Edge Cases:
Handles zero values gracefully, treating them as valid inputs.
Ensures no unexpected behavior for invalid data types (like strings, None, or negative numbers).

Volume Calculation:
The volume of the package is calculated as width * height * length.

Bulky Check:
A package is considered bulky if its volume is greater than or equal to 1,000,000 cm³ or if any of its dimensions (width, height, or length) is greater than or equal to 150 cm.

Heavy Check:
A package is considered heavy if its mass is greater than or equal to 20 kg.

Stack Assignment:
REJECTED: If the package is both bulky and heavy.
SPECIAL: If the package is either bulky or heavy, but not both.
STANDARD: If the package is neither bulky nor heavy.

Complexity
Time Complexity: O(1) — The function performs a constant number of operations regardless of input size.
Space Complexity: O(1) — The function uses a fixed amount of memory.

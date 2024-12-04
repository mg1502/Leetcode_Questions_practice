class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev_value = 0
        for char in reversed(s):  # Traverse the string in reverse
            current_value = roman_values[char]
            if current_value < prev_value:  # If smaller, subtract
                total -= current_value
            else:  # If larger or equal, add
                total += current_value
            prev_value = current_value  # Update previous value
        return total
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum  = 0
        n = len(s)

        for i in range(n):
            current_value = roman_to_int[s[i]]
            if i == n -1 or current_value >= roman_to_int[s[i + 1]]:
                sum += current_value
            else:
                sum -= current_value
        return sum

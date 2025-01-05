class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        net_shifts = [0] * (n + 1)  # Difference array to store cumulative shifts

        # Populate the difference array
        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            net_shifts[start] += shift
            if end + 1 < n:
                net_shifts[end + 1] -= shift

        # Calculate the prefix sum to get the final shifts
        for i in range(1, n):
            net_shifts[i] += net_shifts[i - 1]

        # Apply the shifts to the string
        result = []
        for i, char in enumerate(s):
            new_char = chr((ord(char) - ord('a') + net_shifts[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)



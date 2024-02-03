# Problem : Sequential Digits
# Problem Statement : An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    result.append(num)
        return sorted(result)

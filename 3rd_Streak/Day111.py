# Problem : Number of Atoms
# Problem Statement : Given a string formula representing a chemical formula, return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.
# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.
# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
# The test cases are generated so that all the values in the output fit in a 32-bit integer.
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = defaultdict(int)
        stack = [1]
        element, num = "", ""
        for i in range(len(formula) - 1, -1, -1):
            c = formula[i]
            if c.isdigit():
                num = c + num
            elif c.islower():
                element = c
            elif c.isupper():
                counts[c + element] += (int(num) if num else 1) * stack[-1]
                element, num = "", ""
            elif c == ")":
                stack.append((int(num) if num else 1) * stack[-1])
                num = ""
            elif c == "(":
                stack.pop()
        return "".join(
            key + (str(freq) if freq > 1 else "")
            for key, freq in sorted(counts.items())
        )

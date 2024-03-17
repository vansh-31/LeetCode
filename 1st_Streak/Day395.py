# Problem :
# Problem Statement : You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        for i in tokens:
            if i.isnumeric() or (i[0] == "-" and i[1:].isnumeric()):
                s.append(int(i))
            elif i in ["+", "-", "*", "/"]:
                op2 = s.pop()
                op1 = s.pop()
                if i == "+":
                    res = op1 + op2
                elif i == "-":
                    res = op1 - op2
                elif i == "*":
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                s.append(res)
        return s.pop()

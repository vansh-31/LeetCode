# Problem : Validate Stack Sequences
# Problem Statement : Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i = j = 0
        k = -1
        while i < len(pushed) and j < len(popped):
            if pushed[i] == popped[j]:
                i += 1
                j += 1
                continue
            if k >= 0 and stack[k] == popped[j]:
                k-=1
                j+=1
                stack.pop()
                continue
            stack.append(pushed[i])
            k+=1
            i+=1
        i = len(stack) - 1
        while j < len(popped) and i >= 0:
            if stack[i] != popped[j]:
                return False
            j+=1
            i-=1
        return True
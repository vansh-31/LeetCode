# Problem : Implement Queue using Stacks
# Problem Statement : Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.


# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
class MyQueue(object):
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
        self.front = -1

    def push(self, x):
        if not self.in_stk and self.front == -1:
            self.front = x
        self.in_stk.append(x)

    def pop(self):
        if not self.out_stk:
            self.switch_stack()
        x = self.out_stk.pop()
        self.front = -1
        if self.out_stk:
            self.front = self.out_stk[-1]
        elif self.in_stk:
            self.front = self.in_stk[0]
        return x

    def peek(self):
        return self.front

    def empty(self):
        return not self.in_stk and not self.out_stk

    def switch_stack(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

'''
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

min operation will never be called if there is no number in the stack.

Have you met this question in a real interview?  
Example
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1
'''

class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.min_stack or self.min_stack[-1] >= number:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        number = self.stack.pop()
        if number == self.min_stack[-1]:
            self.min_stack.pop()
        return number

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_stack[-1]

min_stack = MinStack()
min_stack.push(1)
print(min_stack.pop()) # 1
min_stack.push(2)
min_stack.push(3)
print(min_stack.min()) # 2
min_stack.push(1)
print(min_stack.min()) # 1

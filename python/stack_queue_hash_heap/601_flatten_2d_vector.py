'''
Implement an iterator to flatten a 2d vector.

Have you met this question in a real interview?  
Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
'''

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here

        self.row = 0
        self.col = 0
        self.data = vec2d
        self.has_next = True
        if not vec2d:
            self.has_next = False
            return
        self.check_empty_row()

    # @return {int} a next element
    def next(self):
        # Write your code here
        res = self.data[self.row][self.col]
        if len(self.data[self.row]) == self.col + 1:
            if len(self.data) == self.row + 1:
                self.has_next = False
            else:
                self.col = 0
                self.row += 1
                self.check_empty_row()
        else:
            self.col += 1
        return res


        # @return {boolean} true if it has next element
        # or false
    def hasNext(self):
        # Write your code here
        return self.has_next

    def check_empty_row(self):
        while not self.data[self.row]:
            self.row += 1
            if self.row == len(self.data):
                self.has_next = False
                return

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

vec2d = [
    [1, 2],
    [3],
    [4, 5, 6]
]
vec2d = [[], [1, 2], []]
i, v = Vector2D(vec2d), []
while i.hasNext():
    v.append(i.next())
print(v)

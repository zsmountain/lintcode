'''
Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Have you met this question in a real interview?  
Example
Given k = 3 1d vectors:

[1,2,3]
[4,5,6,7]
[8,9]
Return [1,4,8,2,5,9,3,6,7].
'''

import heapq

class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.data = [(j, i, vecs[i][j]) for i in range(len(vecs)) for j in range(len(vecs[i]))]
        heapq.heapify(self.data)
        

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        return heapq.heappop(self.data)[2]

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.data) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result

vecs = [[1, 2, 3],
        [4, 5, 6, 7],
        [8, 9]]
solution, result = ZigzagIterator2(vecs), []
while solution.hasNext():
    result.append(solution.next())
print(result)

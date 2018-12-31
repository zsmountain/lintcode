'''
Given k sorted integer arrays, merge them into one sorted array.

Have you met this question in a real interview?  
Example
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.
'''

import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # write your code here
        data, res = [], []
        for array in arrays:
            for num in array:
                heapq.heappush(data, num)
        while data:
            res.append(heapq.heappop(data))
        return res

s = Solution()
print(s.mergekSortedArrays([
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
]))


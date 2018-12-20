'''
Given an integer array, find the top k largest numbers in it.

Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
'''

import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        # write your code here
        heap = []
        res = []
        for num in nums:
            heapq.heappush(heap, -num)
        for i in range(k):
            res.append(-heapq.heappop(heap))
        return res

s = Solution()
print(s.topk([3, 10, 1000, -99, 4, 100], 3))

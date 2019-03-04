'''
Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

Have you met this question in a real interview?  
Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

Challenge
o(n) time and O(k) memory
'''

from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or k < 1:
            return []
        
        q = deque()
        res = []
        for i in range(k - 1):
            self.push(q, nums, i)
        for i in range(k - 1, len(nums)):
            self.push(q, nums, i)
            res.append(nums[q[0]])
            if q[0] == i - k + 1:
                q.popleft()
        return res

    def push(self, q, nums, i):
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)

s = Solution()
print(s.maxSlidingWindow([1, 2, 7, 7, 8], 3))

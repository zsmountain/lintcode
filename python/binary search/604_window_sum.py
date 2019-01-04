'''
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Have you met this question in a real interview?  
Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
'''

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if len(nums) < k or k == 0:
            return []
        res = []
        sum = 0
        for i in range(k):
            sum += nums[i]
        res.append(sum)
        for i in range(len(nums) - k + 1 ):
            if i + k >= len(nums):
                break
            sum = sum - nums[i] + nums[i + k]
            res.append(sum)
        return res

s = Solution()
print(s.winSum([1, 2, 7, 7, 2], 1))
print(s.winSum([1, 2, 7, 8, 5], 3))
print(s.winSum([1, 2, 3], 3))

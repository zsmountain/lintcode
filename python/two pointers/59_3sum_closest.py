'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Have you met this question in a real interview?  
Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge
O(n^2) time, O(1) extra space
'''

import math

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers:
            return 0
        if len(numbers) <= 3:
            return sum(numbers)
        numbers.sort()
        res = 0
        dist = math.inf
        for i in range(len(numbers) - 1):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                three_sum = numbers[i] + numbers[left] + numbers[right]
                if three_sum == target:
                    return target
                if (abs(three_sum - target)) < dist:
                    dist = abs(three_sum - target)
                    res = three_sum
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        return res

s = Solution()
numbers = [-1, 2, 1, -4]
print(s.threeSumClosest(numbers, 1))

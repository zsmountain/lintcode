'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Have you met this question in a real interview?  
Clarification
Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
'''

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        # write your code here
        num_set = set()
        res = 0
        for n in num:
            num_set.add(n)
        for n in num:
            left = right = n
            while left in num_set:
                num_set.remove(left)
                left -= 1
            num_set.add(n)
            while right in num_set:
                num_set.remove(right)
                right += 1
            res = max(res, right - left - 1)
        return res

s = Solution()
num = [1, 2, 0, 1]
print(s.longestConsecutive(num))
num = [100, 4, 200, 1, 3, 2]
print(s.longestConsecutive(num))

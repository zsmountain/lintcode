'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

Have you met this question in a real interview?  
Example
Given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:

(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
'''

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        # write your code here
        res = []
        length = len(numbers)
        if length < 4:
            return res
        numbers.sort()
        for i in range(length - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    if numbers[i] + numbers[j] + numbers[left] + numbers[right] < target:
                        left += 1
                    elif numbers[i] + numbers[j] + numbers[left] + numbers[right] > target:
                        right -= 1
                    else:
                        res.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1
                        right -= 1
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1
        return res

s = Solution()
print(s.fourSum([1, 0, -1, 0, 0, -2, 2], 0))

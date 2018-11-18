'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        res = []
        if len(numbers) < 3:
            return res
        numbers.sort()
        for i in range(len(numbers) - 2):
            if i and numbers[i] == numbers[i-1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[i] + numbers[left] + numbers[right] == 0:
                    res.append((numbers[i], numbers[left], numbers[right]))
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left-1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                
                elif numbers[i] + numbers[left] + numbers[right] < 0:
                    left += 1
                else:
                    right -= 1
        return res

s = Solution()
print(s.threeSum([-2, -3, 5, -1, -4, 5, -11, 7, 1, 2, 3, 4, -7, -1, -2, -3, -4, -5]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

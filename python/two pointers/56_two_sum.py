'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

You may assume that each input would have exactly one solution

Have you met this question in a real interview?  
Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        pairs = [(numbers[i], i) for i in range(len(numbers))]
        pairs.sort(key=lambda x: x[0])
        left, right = 0, len(numbers) - 1
        while left < right:
            if pairs[left][0] + pairs[right][0] == target:
                return [min(pairs[left][1], pairs[right][1]), max(pairs[left][1], pairs[right][1])]
            if pairs[left][0] + pairs[right][0] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))

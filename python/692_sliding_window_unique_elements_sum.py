'''
Given an array and a window size that is sliding along the array, find the sum of the count of unique elements in each window.

If the window size is larger than the length of array, just regard it as the length of the array (i.e., the window won't slide).
Have you met this question in a real interview?  
Example
Example1

Input:
[1, 2, 1, 3, 3]
3
Output: 5
Explanation:
First window [1, 2, 1], only 2 is unique, count is 1.
Second window [2, 1, 3], all elements unique, count is 3.
Third window [1, 3, 3], only 1 is unique, count is 1.
sum of count = 1 + 3 + 1 = 5
Example1

Input:
[1, 2, 1, 2, 1]
3
Output: 3
'''

class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """

    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        count_mapping = {}
        res = []
        for i in range(min(k, len(nums))):
            count_mapping[nums[i]] = count_mapping.get(nums[i], 0) + 1
        count = 0
        for cnt in count_mapping.values():
            if cnt == 1:
                count += 1
        res.append(count)
        if (k > len(nums)):
            return count
        left = 0
        for i in range(k, len(nums)):
            count_mapping[nums[left]] -= 1
            if count_mapping[nums[left]] == 1:
                count += 1
            if count_mapping[nums[left]] == 0:
                count -= 1
            count_mapping[nums[i]] = count_mapping.get(nums[i], 0) + 1
            if count_mapping[nums[i]] == 1:
                count += 1
            if count_mapping[nums[i]] == 2:
                count -= 1
            left += 1
            res.append(count)
        return sum(res)

s = Solution()
print(s.slidingWindowUniqueElementsSum([47, 13, 40, 40, 48, 45, 40], 5))
print(s.slidingWindowUniqueElementsSum([1, 2, 1, 3, 3], 3))
print(s.slidingWindowUniqueElementsSum([1, 2, 1, 3, 3], 6))
print(s.slidingWindowUniqueElementsSum([1, 2, 1, 2, 1], 3))
        

'''
Given an array, return the shortest subarray length which has duplicate elements.

If the array doesn't ha the subarray which has duplicate elements, return -1.

0 <= arr.length <= 10^6
Have you met this question in a real interview?  
Example
Example 1:

Input: [1,2,3,1,4,5,4,6,8]
Output: 3
Explanation: The the shortest subarray which has duplicate elements is [4,5,4].
Example 2:

Input: [1,1]
Output: 2
Explanation: The the shortest subarray which has duplicate elements is [1,1].
'''

import math

class Solution:
    """
    @param arr: The array you should find shortest subarray length which has duplicate elements.
    @return: Return the shortest subarray length which has duplicate elements.
    """
    def getLength(self, arr):
        # Write your code here.
        mapping = {}
        start, end, minLength = 1, -1, math.inf
        for i, num in enumerate(arr):
            if num in mapping and i - mapping[num] < minLength:
                    minLength = i - mapping[num]
                    start, end = mapping[num], i
            mapping[num] = i
        return end + 1 - start

s = Solution()
print(s.getLength([1, 2, 3, 1, 4, 5, 4, 6, 8]))
print(s.getLength([1, 1]))
print(s.getLength([1, 2]))

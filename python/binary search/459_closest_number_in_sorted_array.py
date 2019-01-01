'''
Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

There can be duplicate elements in the array, and we can return any of the indices with same value.

Have you met this question in a real interview?  
Example
Given [1, 2, 3] and target = 2, return 1.

Given [1, 4, 6] and target = 3, return 1.

Given [1, 4, 6] and target = 5, return 1 or 2.

Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.

Challenge
O(logn) time complexity.
'''

class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """

    def closestNumber(self, A, target):
        # write your code here
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                return mid
        return start if abs(A[start] - target) < abs(A[end] - target) else end

s = Solution()
print(s.closestNumber([1, 4, 8, 12, 16, 28, 38], 26))
print(s.closestNumber([1, 2, 3], 2))
print(s.closestNumber([1, 4, 6], 3))
print(s.closestNumber([1, 4, 6], 5))
print(s.closestNumber([1, 3, 3, 4], 2))

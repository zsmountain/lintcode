'''
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.
'''

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        res = []
        if not A:
            return res
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if (A[mid] <= target):
                start = mid
            else:
                end = mid

        for i in range(k):
            if start < 0:
                res.append(A[end])
                end += 1
                continue
            if end > len(A) - 1:
                res.append(A[start])
                start -= 1
                continue
            if (abs(A[start] - target) <= abs(A[end] - target)):
                res.append(A[start])
                start -= 1
            else:
                res.append(A[end])
                end += 1
        return res

s = Solution()
print(s.kClosestNumbers([1, 2, 3], 2, 3))
print(s.kClosestNumbers([1, 4, 6, 8], 3, 3))
print(s.kClosestNumbers([1, 3], 2, 2))
                        
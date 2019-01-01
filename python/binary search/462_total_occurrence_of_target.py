'''
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Have you met this question in a real interview?  
Example
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.

Challenge
Time complexity in O(logn)
'''

class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        # write your code here
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target: 
                end = mid
            else:
                left_end = right_start = mid
                while start + 1 < left_end:
                    mid = (start + left_end) // 2
                    if A[mid] < target:
                        start = mid
                    else:
                        left_end = mid
                left = start if A[start] == target else left_end
                while right_start + 1 < end:
                    mid = (right_start + end) // 2
                    if A[mid] > target:
                        end = mid
                    else:
                        right_start = mid
                right = end if A[end] == target else right_start
                return right - left + 1
        return 0

s = Solution()
print(s.totalOccurrence([1, 2, 3, 3, 4, 5], 3))
print(s.totalOccurrence([2, 2, 3, 4, 6], 4))
print(s.totalOccurrence([1, 2, 3, 4, 5], 6))
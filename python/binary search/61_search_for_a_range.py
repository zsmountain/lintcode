'''
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Have you met this question in a real interview?  
Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Challenge
O(log n) time.
'''

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
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
                return [left, right]
        if A[start] == target:
            return [start, start]
        elif A[end] == target:
            return [end, end]
        else:
            return [-1, -1]

s = Solution()
A = [1]
print(s.searchRange(A, 1))
A = [5, 7, 7, 8, 8, 10]
print(s.searchRange(A, 8))

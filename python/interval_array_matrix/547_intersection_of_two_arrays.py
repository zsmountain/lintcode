'''
Given two arrays, write a function to compute their intersection.

Each element in the result must be unique.
The result can be in any order.
Have you met this question in a real interview?  
Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Challenge
Can you implement it in three different algorithms?
'''

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        # write your code here
        return list(set(nums1) & set(nums2))

    def intersection(self, nums1, nums2):
        res = []
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if i + 1 < len(nums1) and nums1[i + 1] == nums1[i]:
                i += 1
                continue
            if j + 1 < len(nums2) and nums2[j + 1] == nums2[j]:
                j += 1
                continue
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))

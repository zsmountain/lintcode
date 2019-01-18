'''
Give a number of arrays, find their intersection, and output their intersection size.

The total number of all array elements is not more than 500000.
There are no duplicated elements in each array.
Have you met this question in a real interview?  
Example
Given [[1,2,3],[3,4,5],[3,9,10]], return 1

explanation:
Only element 3 appears in all arrays, the intersection is [3], and the size is 1.
Given [[1,2,3,4],[1,2,5,6,7][9,10,1,5,2,3]], return 2

explanation:
Only element 1,2 appear in all arrays, the intersection is [1,2], the size is 2.
'''

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        # write your code here
        hash = {}
        res = 0
        size = len(arrs)
        for arr in arrs:
            for num in arr:
                if num in hash:
                    hash[num] += 1
                else:
                    hash[num] = 1
        for key, val in hash.items():
            if val == size:
                res += 1
        return res

s = Solution()
print(s.intersectionOfArrays([[1, 2, 3], [3, 4, 5], [3, 9, 10]]))

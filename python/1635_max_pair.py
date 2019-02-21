'''
Give two Lists, give a maximum value, find a bunch in each of the two lists, and find all the pairs that are closest to the maximum but not larger than the maximum.

The length of the two lists do not exceed 100000100000.
Each element do not exceed 10000000001000000000.

Have you met this question in a real interview?  
Example
Give a=[2,3,4,5,6], b=[4,5,7], x=8', return [[3,5],[4,4]].

Explanation:
the sum of [3,5] or [4,4] is 8, which is no larger than 8. 
Give a=[2,3,4,5,6], b=[4,5,7], x=10', return [[3,7],[5,5],[6,4]].

Explanation:
the sum of [3,7],[5,5],[6,4] is 10, which is no larger than 10. 
'''

class Solution:
    """
    @param a: the first list
    @param b: the second list
    @param x: the max sum
    @return: the pairs whose sum are not exceed x
    """
    def getAns(self, a, b, x):
        # Write your code here.
        a.sort()
        b.sort()
        left, right = 0, len(b) - 1
        res = []
        max = 0
        while left < len(a) and right >= 0:
            if a[left] + b[right] > x:
                right -= 1
            else:
                if a[left] + b[right] == max:
                    res.append([a[left], b[right]])
                elif a[left] + b[right] > max:
                    res = [[a[left], b[right]]]
                    max = a[left] + b[right]
                left += 1
        return res

s = Solution()
print(s.getAns([2, 3, 4, 5, 6], [4, 5, 7], 8))
print(s.getAns([2, 3, 4, 5, 6], [4, 5, 7], 10))
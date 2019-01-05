'''
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

Have you met this question in a real interview?  
Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
'''


class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        res = 0
        S.sort()
        for i in range(len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] <= S[i]:
                    left += 1
                else:
                    res += right - left
                    right -=1
        return res

s = Solution()
print(s.triangleCount([3, 4, 5, 7]))
print(s.triangleCount([4, 4, 4, 4]))


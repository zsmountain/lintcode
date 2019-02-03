'''
Given an integer array, find a subarray where the sum of numbers is in a given interval. Your code should return the number of possible answers. (The element in the array should be positive)

题目中数组内的元素保证都是正数

Have you met this question in a real interview?  
Example
Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

[0, 0]
[0, 1]
[1, 1]
[2, 2]
'''

class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    def subarraySumII(self, A, start, end):
        # write your code here
        #A.sort()
        prefix_sum = [0]
        for num in A:
            prefix_sum.append(prefix_sum[-1] + num)


        left, right, res = 0, 0, 0
        for i in range(len(A)):
            while left < i + 1 and prefix_sum[i+1] - prefix_sum[left] > end:
                left +=1
            while right < i + 1 and prefix_sum[i+1] - prefix_sum[right] >= start:
                right += 1
            res += right - left

        return res

s = Solution()
print(s.subarraySumII([1, 2, 3, 4], 1, 3))
print(s.subarraySumII([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 10))
print(s.subarraySumII([1, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5], 1, 19))

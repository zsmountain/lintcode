'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Have you met this question in a real interview?  
Example
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Example 2:

Input: [9,9,9]
Output: [1,0,0,0]
'''

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        c = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1 + c if i == len(digits) - 1 else digits[i] + c
            if digits[i] == 10:
                digits[i] = 0
                c = 1
            else:
                c = 0
        if c:
            digits.insert(0, 1)
        return digits

s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([9, 9, 9]))

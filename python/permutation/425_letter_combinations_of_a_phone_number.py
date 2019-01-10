'''
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Cellphone

Although the above answer is in lexicographical order, your answer could be in any order you want.

Example
Given "23"

Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
'''

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        self.helper(digits, 0, res, '', mapping)
        return res

    def helper(self, digits, index, res, cur, mapping):
        if len(digits) == index:
            res.append(cur)
            return
        for ch in mapping[int(digits[index])]:
            self.helper(digits, index + 1, res, cur + ch, mapping)

s = Solution()
print(s.letterCombinations('23'))
print(s.letterCombinations(''))

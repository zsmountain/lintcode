'''
Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

Have you met this question in a real interview?  
Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz
'''

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        number = ''
        stack = []
        for ch in s:
            if ch.isdigit():
                number += ch
            elif ch == '[':
                stack.append(int(number))
                number = ''
            elif ch == ']':
                string = ''
                while not isinstance(stack[-1], int):
                    string += stack.pop()
                count = stack.pop()
                for i in range(count):
                    stack.append(string)
            else:
                stack.append(ch)
        return self.popStack(stack)

    def popStack(self, stack):
        string = ''
        while stack and not isinstance(stack[-1], int):
            string += stack.pop()
        return string[::-1]
        
s = Solution()
print(s.expressionExpand('abc3[a]'))
print(s.expressionExpand('3[abc]'))
print(s.expressionExpand('4[ac]dy'))
print(s.expressionExpand('3[2[ad]3[pf]]xyz') == 'adadpfpfpfadadpfpfpfadadpfpfpfxyz')

'''
Giving a string with number from 1-n in random order, but miss 1 number.Find that number.

n <= 30

Have you met this question in a real interview?  
Example
Given n = 20, str = 19201234567891011121314151618

return 17
'''

class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        # write your code here
        visited = set()
        return self.helper(n, str, visited)

    def helper(self, n, str, visited):
        if len(visited) == n - 1 and not str:
            for i in range(1, n + 1):
                if i not in visited:
                    return i 

        if not str or str[0] == '0':
            return -1

        for i in range(1, 3):
            num = int(str[0:i])
            if 0 < num <= n and num not in visited:
                visited.add(num)
                found = self.helper(n, str[i:], visited)
                if found > 0:
                    return found
                visited.remove(num)
        return -1
        
s = Solution()
print(s.findMissing2(13, '1110987654321213'))
print(s.findMissing2(11, '111098765432'))
print(s.findMissing2(20, '19201234567891011121314151618'))

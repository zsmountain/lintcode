'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Have you met this question in a real interview?  
Example
Given "25525511135", return

[
  "255.255.11.135",
  "255.255.111.35"
]
Order does not matter.
'''

class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        # write your code here
        res = []
        self.helper(s, res, '', 0)
        return res

    def helper(self, s, res, cur, seg):
        if seg == 4 and not s:
            res.append(cur)
            return

        if seg >= 4 or not s:
            return

        for i in range(1, 4):
            if i > len(s):
                continue
            if i > 1 and s[0] == '0':
                continue
            ip = s[0:i]
            if int(ip) <= 255:
                self.helper(s[i:], res, cur + '.' + ip if cur else ip, seg + 1)

s = Solution()
print(s.restoreIpAddresses('25525511135'))
print(s.restoreIpAddresses('00255111'))

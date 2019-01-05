'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''

from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        q = deque([start])
        res = 0
        visited = set()
        while q:
            res += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur == end:
                    return res
                for word in self.get_next_words(cur, dict, visited):
                    q.append(word)

        return 0

    def get_next_words(self, word, dict, visited):
        res = []
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == word[i]:
                    continue
                next_word = word[:i] + ch + word[i+1:]
                if next_word in dict and not next_word in visited:
                    res.append(next_word)
                    visited.add(next_word)
        return res

s = Solution()
print(s.ladderLength('hit', 'cog', set(['hot', 'dot', 'dog', 'lot', 'log'])))

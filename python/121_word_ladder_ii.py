'''
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
All words have the same length.
All words contain only lowercase alphabetic characters.
Have you met this question in a real interview?  
Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return

[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
'''

from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        # write your code here
        if not start or not end or not dict:
            return []
        distance = {}
        res = []
        dict.add(start)
        dict.add(end)
        self.bfs(start, end, dict, distance)
        self.dfs(end, dict, distance, res, [start])
        return res

    def dfs(self, end, dict, distance, res, path):
        cur = path[-1]
        if cur == end:
            res.append(path[:])
        for word in self.get_next(cur, dict):
            if distance[word] < distance[cur]:
                path.append(word)
                self.dfs(end, dict, distance, res, path)
                path.pop()

    def bfs(self, start, end, dict, distance):
        q = deque([end])
        distance[end] = 0
        while q:
            word = q.popleft()
            for next_word in self.get_next(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    q.append(next_word)

    def get_next(self, word, dict):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i in range(len(word)):
            for ch in chars:
                if ch == word[i]:
                    continue
                next_word = word[:i] + ch + word[i+1:]
                if next_word in dict:
                    res.append(next_word)
        return res

s = Solution()
print(s.findLadders('hit', 'cog', set(['hot', 'dot', 'dog', 'lot', 'log'])))

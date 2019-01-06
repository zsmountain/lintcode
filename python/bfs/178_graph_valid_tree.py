'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview?  
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
'''

from collections import deque

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        
        neighbors = [[] for i in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        visited = set([0])
        q = deque([0])

        while q:
            node = q.popleft()
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

        return len(visited) == n
            

s = Solution()
print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))


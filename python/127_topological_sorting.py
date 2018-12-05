'''
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.

Have you met this question in a real interview?  
Clarification
Learn more about representation of graphs

Example
For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?
'''

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

import helper

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        degrees = {node: 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                degrees[neighbor] += 1
        
        q = deque()
        for degree in degrees:
            if degrees[degree] == 0:
                q.append(degree)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for node in cur.neighbors:
                degrees[node] -= 1
                if degrees[node] == 0:
                    q.append(node)

        return res


graph = helper.createGraph('0,1,2,3,4#1,3,4#2,1,4#3,4#4')
helper.printGraph(graph)
s = Solution()
print([node.label for node in s.topSort(graph)])

graph = helper.createGraph('0,1,2,3#1,4#2,4,5#3,4,5#4#5')
helper.printGraph(graph)
s = Solution()
print([node.label for node in s.topSort(graph)])

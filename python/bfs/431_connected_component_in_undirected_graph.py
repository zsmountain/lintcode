'''
Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

Each connected component should sort by label.

Have you met this question in a real interview?  
Clarification
Learn more about representation of graphs

Example
Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
'''

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))


load_src("helper", "../helper.py")
from helper import UndirectedGraphNode

from collections import deque

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes):
        # write your code here
        res = []
        if not nodes:
            return res

        q = deque()
        visited = set()

        for node in nodes:
            if node not in visited:
                q.append(node)
                visited.add(node)
                row = []
                while q:            
                    node = q.popleft()
                    row.append(node.label)
                    for neighbor in node.neighbors:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                row.sort()
                res.append(row)

        return res



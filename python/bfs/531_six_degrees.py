'''
Six degrees of separation is the theory that everyone and everything is six or fewer steps away, by way of introduction, from any other person in the world, so that a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps.

Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.

Have you met this question in a real interview?  
Example
Gien a graph:

1------2-----4
 \          /
  \        /
   \--3--/
{1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 return 2

Gien a graph:

1      2-----4
             /
           /
          3
{1#2,4#3,4#4,2,3} and s = 1, t = 4 return -1
'''

"""
Definition for Undirected graph node
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
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        # write your code here
        if not graph or not s or not t:
            return -1

        if s is t:
            return 0

        visited = set([s])
        q = deque([s])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in node.neighbors:
                    if neighbor is t:
                        return level
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        return -1




'''
Given a list of numbers, construct a BST from it(you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two given nodes.

If two nodes do not appear in the BST, return -1
We guarantee that there are no duplicate nodes in BST
The node distance means the number of edges between two nodes
Have you met this question in a real interview?  
Example
input:
numbers = [2,1,3]
node1 = 1
node2 = 3
output:
2
'''

def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src("helper", "../helper.py")
from helper import TreeNode, createTree

class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        root, has_node1, has_node2 = self.construct_bst(numbers, node1, node2)
        if not has_node1 or not has_node2:
            return -1
        lca = self.find_lca(root, node1, node2)
        return self.get_dist(lca, node1) + self.get_dist(lca, node2)

    def construct_bst(self, numbers, node1, node2):
        if not numbers:
            return [None, False, False]
        root = TreeNode(numbers[0])
        has_node1, has_node2 = False, False
        if root.val == node1:
            has_node1 = True
        elif root.val == node2:
            has_node2 = True
        for i in range(1, len(numbers)):
            if numbers[i] == node1:
                has_node1 = True
            elif numbers[i] == node2:
                has_node2 = True
            self.add_node(root, numbers[i])
        return [root, has_node1, has_node2]
            
    def add_node(self, root, number):
        if not root:
            return TreeNode(number)
        if root.val > number:
            root.left = self.add_node(root.left, number)
        else:
            root.right = self.add_node(root.right, number)
        return root

    def find_lca(self, root, node1, node2):
        if not root:
            return None
        if root.val == node1 or root.val == node2:
            return root
        if node1 < root.val and node2 < root.val:
            return self.find_lca(root.left, node1, node2)
        elif node1 > root.val and node2 > root.val:
            return self.find_lca(root.right, node1, node2)
        else:
            return root
    
    def get_dist(self, root, node):
        if not root:
            return 0
        if root.val == node:
            return 0
        if root.val > node:
            return 1 + self.get_dist(root.left, node)
        else:
            return 1 + self.get_dist(root.right, node)

s = Solution()
print(s.bstDistance([2, 1, 3], 1, 3))
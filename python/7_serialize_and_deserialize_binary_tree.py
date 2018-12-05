'''
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

Have you met this question in a real interview?  
Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import helper
TreeNode = helper.TreeNode

from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if not cur:
                    res.append('#')
                else:
                    res.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
        return res
        
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        node_list = []
        root = TreeNode(data[0])
        node_list.append(root)
        index = 0
        is_left = True
        for i in range(1, len(data)):
            val = data[i]
            if val != '#':
                node = TreeNode(val)
                if is_left:
                    node_list[index].left = node
                else:
                    node_list[index].right = node
                node_list.append(node)
            if not is_left:
                index += 1
            is_left = not is_left
        return root

'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

1.The array is only modifiable by the update function.
2.You may assume the number of calls to update and sumRange function is distributed evenly.

Have you met this question in a real interview?  
Example
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
'''

class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.left = self.right = None
        self.start = start
        self.end = end
        self.sum = sum

class SegmentTree:
    def build(self, nums):
        return self.buildHelper(nums, 0, len(nums) - 1)

    def buildHelper(self, nums, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, nums[start])
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = self.buildHelper(nums, start, mid)
        root.right = self.buildHelper(nums, mid + 1, end)
        left_sum = root.left.sum if root.left else 0
        right_sum = root.right.sum if root.right else 0
        root.sum = left_sum + right_sum
        return root
    
    def query(self, root, start, end):
        if start > end:
            return 0
        if root.start == start and root.end == end:
            return root.sum
        mid = (root.start + root.end) // 2
        left_sum, right_sum = 0, 0
        if start <= mid:
            left_sum = self.query(root.left, start, min(mid, end))
        if end > mid:
            right_sum = self.query(root.right, max(start, mid + 1), end)
        return left_sum + right_sum

    def update(self, root, index, val):
        if root.start == index and root.end == index:
            root.sum = val
            return
        mid = (root.start + root.end) // 2
        if root.start <= index <= mid:
            self.update(root.left, index, val)
        if root.end >= index > mid:
            self.update(root.right, index, val)
        root.sum = root.left.sum + root.right.sum

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = SegmentTree()
        self.root = self.tree.build(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.tree.update(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.query(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
print(numArray.sumRange(0, 2))

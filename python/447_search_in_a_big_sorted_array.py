'''
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.

Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.
'''

class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def __init__(self, reader):
        self.reader = reader

    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 1
        while self.get(index) < target:
            index *= 2
        start, end = index // 2, index
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get(mid) < target:
                start = mid
            else:
                end = mid

        if self.get(start) == target:
            return start
        if self.get(end) == target:
            return end
        return -1

    def get(self, index):
        return self.reader[index]

s = Solution([1, 3, 6, 9, 21])
print(s.searchBigSortedArray([1, 3, 6, 9, 21], 3))
print(s.searchBigSortedArray([1, 3, 6, 9, 21], 4))
print(s.searchBigSortedArray([1, 3, 6, 9, 21], 1))
s = Solution([0, 0, 1, 1])
print(s.searchBigSortedArray([0, 0, 1, 1], 0))
print(s.searchBigSortedArray([0, 0, 1, 1], 1))

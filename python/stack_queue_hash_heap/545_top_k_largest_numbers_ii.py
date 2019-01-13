'''
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
Have you met this question in a real interview?  
Example
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
'''

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k 
        self.data = [0 for _ in range(k + 2)]

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        self.data[0] += 1
        new_pos = self.data[0]
        self.data[new_pos] = num
        parent_pos = new_pos // 2
        while parent_pos:
            if self.data[parent_pos] > self.data[new_pos]:
                self.data[parent_pos], self.data[new_pos] = self.data[new_pos], self.data[parent_pos]
            else:
                break
            parent_pos = parent_pos // 2
            new_pos = new_pos // 2
        if self.data[0] == self.k + 1:
            self.pop()

    def pop(self):
        if self.data[0] == 0:
            raise Exception('pop from empty')
        res = self.data[1]
        self.data[self.data[0]], self.data[1] = self.data[1], self.data[self.data[0]]
        pos = 1
        self.data[0] -= 1
        while self.data[0] >= pos * 2:
            min_index = pos
            left = pos * 2 
            right = pos * 2 + 1

            if self.data[0] >= left and self.data[left] < self.data[min_index]:
                min_index = left

            if self.data[0] >= right and self.data[right] < self.data[min_index]:
                min_index = right

            if min_index == pos:
                break

            self.data[min_index], self.data[pos] = self.data[pos], self.data[min_index]
            pos = min_index

        return res

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.data[1:self.data[0] + 1], reverse=True)


s = Solution(3)
s.add(3)
s.add(10)
print(s.topk()) # [10, 3]
s.add(1000)
s.add(-99)
print(s.topk()) #[1000, 10, 3]
s.add(4)
print(s.topk()) # [1000, 10, 4]
s.add(100)
print(s.topk()) #[1000, 100, 10]

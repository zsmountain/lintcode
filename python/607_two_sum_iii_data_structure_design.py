'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
'''

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    nums = {}

    def add(self, number):
        # write your code here
        self.nums[number] = self.nums[number] + 1 if number in self.nums else 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for num in self.nums:
            if value - num == num:
                return True if self.nums[num] > 1 else False
            if (value - num) in self.nums:
                return True
        return False

twoSum = TwoSum()

twoSum.add(1)
twoSum.add(3)
twoSum.add(5)
print(twoSum.find(4))
print(twoSum.find(7))
print(twoSum.find(2))

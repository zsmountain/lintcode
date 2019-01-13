'''
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Have you met this question in a real interview?  
Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge
O(n) time complexity
'''

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        for i in range(len(A) // 2, -1, -1):
            self.shift_down(A, i)

    def shift_down(self, A, index):
        while index < len(A):
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            min_index = index

            if left_index < len(A) and A[left_index] < A[min_index]:
                min_index = left_index

            if right_index < len(A) and A[right_index] < A[min_index]:
                min_index = right_index

            if min_index == index:
                break
        
            A[min_index], A[index] = A[index], A[min_index]
            index = min_index

s = Solution()
A = [3, 2, 1, 4, 5]
s.heapify(A)
print(A)

'''
Merge two given sorted integer array A and B into a new sorted integer array.

Have you met this question in a real interview?  
Example
Example 1:
	Input:  A=[1], B=[1]
	Output: [1,1]
	
	Explanation: 
	return array merged.

Example 2:
	Input:  A=[1,2,3,4], B=[2,4,5,6]
	Output: [1,2,2,3,4,4,5,6]
	
	Explanation: 
	return array merged.

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
'''

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        while i < len(A):
            res.append(A[i])
            i += 1
        while j < len(B):
            res.append(B[j])
            j += 1        
        return res

s = Solution()
A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
print(s.mergeSortedArray(A, B))

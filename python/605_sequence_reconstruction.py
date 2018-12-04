'''
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, 
with 1 ≤ n ≤ 10^4. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs 
are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example
Given org = [1,2,3], seqs = [[1,2],[1,3]]
Return false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Given org = [1,2,3], seqs = [[1,2]]
Return false
Explanation:
The reconstructed sequence can only be [1,2].

Given org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Return true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Given org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Return true
'''

from collections import deque

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        edges = {i: [] for i in org}
        degrees = {i: 0 for i in org}
        nodes = set()
        for seq in seqs:
            for i in range(0, len(seq)):
                nodes.add(seq[i])
                if seq[i] > len(org):
                    return False
                if i == 0: 
                   continue
                edges[seq[i - 1]].append(seq[i])
                degrees[seq[i]] += 1

        if len(nodes) != len(org):
            return False
            
        queue = deque()
        for i, degree in degrees.items():                
            if degree == 0:
                queue.append(i)
        
        if len(queue) > 1:
            return False
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for edge in edges[node]:
                degrees[edge] -= 1
                if degrees[edge] == 0:
                    queue.append(edge)
            if len(queue) > 1:
                return False

        if res == org:
            return True
        return False

s = Solution()
print(s.sequenceReconstruction([5, 3, 2, 4, 1],
                               [[5, 3, 2, 4], [4, 1], [1], [3], [2, 4], [1, 1000000000]]))
print(s.sequenceReconstruction([1],  []))
print(s.sequenceReconstruction([1, 2, 3],  [[1, 2], [1, 3]]))
print(s.sequenceReconstruction([1, 2, 3],  [[1, 2]]))
print(s.sequenceReconstruction([1, 2, 3],  [[1, 2], [1, 3], [2, 3]]))
print(s.sequenceReconstruction([4, 1, 5, 2, 6, 3],   [[5, 2, 6, 3], [4, 1, 5, 2]]))
        



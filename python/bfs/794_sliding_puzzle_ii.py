'''
On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.

If it is impossible to move from initial state to final state, return -1.

Have you met this question in a real interview?  
Example
Given an initial state:

[
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
and a final state:

[
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
Return 4
Explanation:

[                 [
 [2,8,3],          [2,0,3],
 [1,0,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [2,0,3],          [0,2,3],
 [1,8,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [0,2,3],          [1,2,3],
 [1,8,4],   -->    [0,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [1,2,3],          [1,2,3],
 [0,8,4],   -->    [8,0,4],
 [7,6,5]           [7,6,5]
]                 ]
Challenge
How to optimize the memory?
Can you solve it with A* algorithm?
'''

from collections import deque

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        # # write your code here
        if not init_state or not init_state[0] or not final_state or not final_state[0]:
            return -1
        if len(init_state) != len(final_state) or len(init_state[0]) != len(final_state[0]):
            return -1

        serialized_final_state = self.serialize(final_state)

        q = deque()
        visited = set()
        for i in range(len(init_state)):
            for j in range(len(init_state[0])):
                if init_state[i][j] == 0:
                    q.append((i,j, self.serialize(init_state)))
                    visited.add(self.serialize(init_state))

        step = 0
        while q:
            for _ in range(len(q)):
                x, y, serialized_state = q.popleft()
                if serialized_state == serialized_final_state:
                    return step
                state = self.deserialize(serialized_state, len(init_state), len(init_state[0]))
                delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in delta:
                    next_x = x + dx
                    next_y = y + dy
                    if 0 <= next_x < len(state) and 0 <= next_y < len(state[0]):
                        state[x][y], state[next_x][next_y] = state[next_x][next_y], state[x][y]
                        serialized_next_state = self.serialize(state)
                        if serialized_next_state not in visited:
                            q.append((next_x, next_y, serialized_next_state))
                            visited.add(serialized_next_state)
                        state[x][y], state[next_x][next_y] = state[next_x][next_y], state[x][y]

            step += 1
                
        return -1
        
    def serialize(self, state):
        res = ''
        for i in range(len(state)):
            for j in range(len(state[0])):
                res += str(state[i][j])
        return res
    
    def deserialize(self, string, m, n):
        res = [[0 for i in range(m)] for j in range(n)]
        index = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = int(string[index])
                index += 1
        return res

s = Solution()
init_state = [
    [2, 8, 3],
    [1, 0, 4],
    [7, 6, 5]
]
final_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

print(s.minMoveStep(init_state, final_state))

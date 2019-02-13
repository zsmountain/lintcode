'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

The solution is guaranteed to be unique.

Have you met this question in a real interview?  
Example
Given 4 gas stations with gas[i]=[1,1,3,1], and the cost[i]=[2,2,1,1]. The starting gas station's index is 2.

Challenge
O(n) time and O(1) extra space
'''

class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """

    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if not gas or not cost or len(gas) != len(cost):
            return -1
        total = sum = 0
        index = -1
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                index = i
                sum = 0
        return -1 if total < 0 else index + 1

s = Solution()
print(s.canCompleteCircuit([2, 0, 1, 2, 3, 4, 0],
                           [0, 1, 0, 0, 0, 0, 11]))
print(s.canCompleteCircuit([1, 1, 3, 1], [2, 2, 1, 1]))
        

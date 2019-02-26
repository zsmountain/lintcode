'''
n rocks (excluding the starting point and the end point), the distance from the i rock to the starting point is d[i], 
and the distance from the end to the starting point is target. From the starting point to the adjacent rocks at each step until the end point, 
what is the maximum value of the shortest jump distance when the maximum number of m blocks of rock can be removed?

Example
Given n=5, m=2, target=25, d=[2,11,14,17,21], return 4.

Remove the first stone and the third stone.
Notice
0 <= m <= n <= 50,000
1 <= target <= 1,000,000,000
These rocks are given in order from small to large distances from the starting point, and no two rocks will appear in the same place.
'''


class Solution:
    """
    @param n: The total number of stones.
    @param m: The total number of stones you can remove.
    @param target: The distance from the end to the starting point.
    @param d: The array that the distance from the i rock to the starting point is d[i].
    @return: Return the maximum value of the shortest jump distance.
    """

    def getDistance(self, n, m, target, d):
        # Write your code here.
        d.append(target)
        d.insert(0, 0)
        left, right = 1, target
        while left <= right:
            mid = (left + right) // 2
            if self.search(d, mid, m, n):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def search(self, d, mid, m, n):
        cnt = 0
        now = 0
        for i in range(1, n + 2):
	        if d[i] - d[now] < mid:
		        cnt += 1
	        else:
		        now = i
        if cnt > m:
	        return False
        else:
	        return True

s = Solution()
print(s.getDistance(5, 2, 25, [2, 11, 14, 17, 21]))

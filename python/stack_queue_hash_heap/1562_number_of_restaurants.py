'''
Give a List of data representing the coordinates[x,y] of each restaurant and the customer is at the origin[0,0]. Find the n restaurants closest to the customer firstly. Then you need to pick n restaurants which appeare firstly in the List and the distance between the restaurant and the customer can't more than the longest distance in the n closest restaurants. Return their coordinates in the original order.

1.Coordinates in range [-1000,1000]
2.n>0
3.No same coordinates

Have you met this question in a real interview?  
Example
Given : n = 2 , List = [[0,0],[1,1],[2,2]]
Return : [[0,0],[1,1]]
Given : n = 3,List = [[0,1],[1,2],[2,1],[1,0]]
Return :[[0,1],[1,2],[2,1]]
'''

from heapq import heappush, heappop

class Solution:
    """
    @param restaurant: 
    @param n: 
    @return: nothing
    """

    def nearestRestaurant(self, restaurant, n):
        # Write your code here
        if not restaurant or n <= 0 or n > len(restaurant):
            return []
        heap = []
        res = []
        for x, y in restaurant:
            heappush(heap, (x * x + y * y, x, y))
        
        nearest_restarant = heappop(heap)
        first_restaurant = [nearest_restarant[1], nearest_restarant[2]]
        for i in range(n - 1):
            nearest_restarant = heappop(heap)
        max_distance = nearest_restarant[0]
        i = 0
        first_restaurant_added = False
        while len(res) < n:
            x, y = restaurant[i]
            if x == first_restaurant[0] and y == first_restaurant[1]:
                first_restaurant_added = True
            if x * x + y * y <= max_distance:
                res.append([x, y])
            i += 1
        if not first_restaurant_added:
            res[-1] = first_restaurant
        return res

s = Solution()
print(s.nearestRestaurant([[111, 11], [121, 2], [133, 31], [1, 224], [1, 35], [121, 12], [132, 13], [124, 14], [31, 15], [12, 245], [
      232, 23], [12, 324], [12, 514], [13, 3], [3, 14], [3, 5], [24, 5], [532, 125], [13, 223], [33, 14], [3, 52], [24, 35]], 4))
print(s.nearestRestaurant([[1, 1]], 2))
print(s.nearestRestaurant([[1, 2]], 1))
print(s.nearestRestaurant([[0, 0], [1, 1], [2, 2]], 2))
print(s.nearestRestaurant([[0, 1], [1, 2], [2, 1], [1, 0]], 3))

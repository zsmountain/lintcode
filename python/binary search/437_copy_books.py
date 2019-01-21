'''
Given n books and the ith book has A[i] pages. You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books. For example one copier can copy the books from ith to jth continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Have you met this question in a real interview?  
Example
Given array A = [3,2,4], k = 2.

Return 5( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )

Challenge
时间复杂度 O(nk)
'''

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.can_finish(pages, k, mid):
                end = mid
            else:
                start = mid
        return start if self.can_finish(pages, k, start) else end

    def can_finish(self, pages, k, time_limit):
        people_count = 1
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                people_count += 1
                time_cost = 0
            time_cost += page

        return people_count <= k

s = Solution()
print(s.copyBooks([3, 2, 4], 2))

'''
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Have you met this question in a real interview?  
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return {1: 72.40, 2: 97.40}
'''

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

import heapq

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        res = {}
        for record in results:
            if record.id not in res:
                res[record.id] = []
            heapq.heappush(res[record.id], -record.score)

        for id in res:
            sum = 0
            for i in range(5):
                sum += heapq.heappop(res[id])
            res[id] = -sum / 5
        return res


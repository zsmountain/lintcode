'''
Given a list of words and an integer k, return the top k frequent words in the list.

You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.

Have you met this question in a real interview?  
Example
Given

[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
for k = 3, return ["code", "lint", "baby"].

for k = 4, return ["code", "lint", "baby", "yes"],

Challenge
Do it in O(nlogk) time and O(n) extra space.
'''

from heapq import heapify, heappush, nsmallest

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        # write your code here
        hash = {}
        heap = []
        for word in words:
            hash[word] = hash.get(word, 0) + 1
        for key, val in hash.items():
            heappush(heap, (-val, key))
        return [item[1] for item in nsmallest(k, heap)]

s = Solution()
words = [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
print(s.topKFrequentWords(words, 3))
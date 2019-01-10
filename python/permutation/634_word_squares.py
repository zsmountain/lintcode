'''
For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Have you met this question in a real interview?  
Example
Given a set ["area","lead","wall","lady","ball"]
return [["wall","area","lead","lady"],["ball","area","lead","lady"]]
return [["wall","area","lead","lady"],["ball","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Given a set ["abat","baba","atan","atal"]
return [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
'''


class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        # write your code here
        res = []
        if not words:
            return res

        prefix = {}
        for w in words:
            for i in range(len(w) + 1):
                if w[0:i] not in prefix:
                    prefix[w[0:i]] = {w}
                else:
                    prefix[w[0:i]].add(w)
        self.helper(words, res, [], prefix)
        return res

    def helper(self, words, res, cur, prefix):
        n = len(words[0])
        if len(cur) == n:
            res.append(cur[:])
            return
        
        row = len(cur)
        head = ''
        for word in cur:
            head += word[row]
        if head not in prefix:
            return

        for word in prefix[head]:
            cur.append(word)
            self.helper(words, res, cur, prefix)
            cur.pop()


s = Solution()
print(s.wordSquares(["area", "lead", "wall", "lady", "ball"]))
print(s.wordSquares(["abat", "baba", "atan", "atal"]))

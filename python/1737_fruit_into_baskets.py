'''
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

1.Add one piece of fruit from this tree to your baskets. If you cannot, stop.
2.Move to the next tree to the right of the current tree. If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
Have you met this question in a real interview?  
Example
Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
'''

class Solution:
    """
    @param tree: The type of fruit
    @return: The total amount of fruit you can collect.
    """
    def totalFruit(self, tree):
        # write your code here
        if len(tree) <= 2:
            return len(tree)
        res = 0
        fruit_in_basket = {}
        for i in range(len(tree)):
            if tree[i] in fruit_in_basket:
                fruit_in_basket[tree[i]][0] += 1
            elif len(fruit_in_basket) <= 1:
                fruit_in_basket[tree[i]] = [1, i]
            else:
                res = max(res, sum([t[0] for t in fruit_in_basket.values()]))
                del fruit_in_basket[tree[min(fruit_in_basket.values(),key=lambda x: x[1])[1]]]
                fruit_in_basket[tree[i]] = [1, i]
        return max(res, sum([t[0] for t in fruit_in_basket.values()]))

s = Solution()
print(s.totalFruit([1, 2, 1]))
print(s.totalFruit([1, 2, 3, 2, 2]))
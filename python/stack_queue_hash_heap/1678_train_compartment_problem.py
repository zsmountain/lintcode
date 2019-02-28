class Solution:
    """
    @param arr: the arr
    @return:  the number of train carriages in this transfer station with the largest number of train carriages
    """

    def trainCompartmentProblem(self, arr):
        # Write your code here.
        if len(arr) <= 1:
            return 0
        stack = []
        count = 0
        curNum = len(arr)
        i = len(arr) - 1
        while i >= 0:
            if arr[i] == curNum:
                curNum -= 1
                if curNum == 0:
                    return count
            elif i > 0 and arr[i] < arr[i-1]:
                stack.append(arr[i])
                count += 1
            else:
                if not stack or stack[-1] != curNum:
                    return -1
                else:
                    stack.pop()
                    curNum -= 1
                    i += 1
            i -= 1
        while stack:
            if curNum != stack.pop():
                return -1
            else:
                curNum -= 1
                if curNum == 0:
                    return count
        return -1

s = Solution()
print(s.trainCompartmentProblem([1, 3, 2, 4, 5, 8, 7, 6]
                                ))
print(s.trainCompartmentProblem([4, 5, 3, 2, 1]))
print(s.trainCompartmentProblem([1, 2, 3, 5, 6, 7, 4]
                                ))

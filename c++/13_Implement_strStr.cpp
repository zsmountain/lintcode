
/*
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
*/

#include "helper.h"

class Solution {
public:
    /**
     * @param source:
     * @param target:
     * @return: return the index
     */
    int strStr(const string &source, const string &target) {
        // Write your code here
        int i = 0, j = 0, lastPos = 0;
        while (i < source.length() && j < target.length()) {
            lastPos = i + 1;
            while (source[i] == target[j]) {
                i++;
                j++;
                if (j == target.length()) {
                    return i - j;
                }
                }
            i = lastPos;
            j = 0;
        }
        if (j == target.length()) {
            return i - j;
        } else {
            return -1;
        }
    }
};

int main() {
    Solution s;
    cout << s.strStr("tartarget", "target") << endl;
    cout << s.strStr("source", "target") << endl;
    cout << s.strStr("abcdabcdefg", "bcd") << endl;
}



/*
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".

Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
*/

#include "helper.h"

class Solution {
public:
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    string longestPalindrome(const string &s) {
        // write your code here
        string res;
        int len = 0;
        for (int i = 0; i< s.length(); i++) {
            string s1 = helper(s, i - 1, i + 1);
            string s2 = helper(s, i, i + 1);
            if (s1.length() > s2.length() && s1.length() > res.length()) {
                res = s1;
            } else if (s2.length() > s1.length() && s2.length() > res.length()) {
                res = s2;
            }
        }
        return res;
    }

    string helper(const string &s, int start, int end) {
        while (start >=0 && end < s.length()) {
            if (s[start] != s[end]) {
                return s.substr(start + 1, end - start - 1);
            } else {
                start--;
                end++;
            }
        }
        return s.substr(start + 1, end);
    }
};


int main() {
    Solution s;
    cout << s.longestPalindrome("abcbd") << endl;
    cout << s.longestPalindrome("abbd") << endl;
    cout << s.longestPalindrome("abcdzdcab") << endl;
    cout << s.longestPalindrome("") << endl;
    cout << s.longestPalindrome("a") << endl;
    cout << s.longestPalindrome("aa") << endl;
    cout << s.longestPalindrome("aaa") << endl;
}


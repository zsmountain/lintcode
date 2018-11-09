
/*
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Assume the length of given string will not exceed 1010.

Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.
*/

#include "helper.h"

class Solution {
public:
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    int longestPalindrome(const string &s) {
        // write your code here
        map<char, int> dict;
        int res = 0;
        int hasOdd = 0;
        for (char c: s) {
            dict[c]++;
        }
        for (auto const &it: dict) {
            if (it.second % 2 == 0) {
                res += it.second;
            } else {
                res += it.second - 1;
                hasOdd = 1;
            }
        }
        return res + hasOdd;
    }
};

int main() {
    Solution s;
    cout << s.longestPalindrome("abccccdd") << endl;
    cout << s.longestPalindrome("") << endl;
    cout << s.longestPalindrome("a") << endl;
    cout << s.longestPalindrome("aaa") << endl;
}

